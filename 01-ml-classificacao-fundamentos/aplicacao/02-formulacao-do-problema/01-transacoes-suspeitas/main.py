"""Laboratório de formulação: classificar transações normais ou suspeitas.

O exemplo usa dados sintéticos para demonstrar a ligação entre:
formulação do problema, dados temporais, baseline, modelo, threshold,
custos e guardrails operacionais.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "amount",
    "hour",
    "account_age_days",
    "transactions_last_24h",
    "distinct_countries_last_7d",
    "device_risk_score",
    "is_international",
    "prior_chargebacks",
    "merchant_risk_score",
]


@dataclass(frozen=True)
class ProblemConfig:
    random_state: int = 42
    n_rows: int = 5_000
    fraud_confirmation_horizon_days: int = 30
    false_positive_cost: float = 5.0
    false_negative_cost: float = 100.0
    # Limite didático para que o guardrail seja acionado nos dados sintéticos.
    high_value_review_limit: float = 1_000.0


def sigmoid(values: np.ndarray) -> np.ndarray:
    """Converte scores em valores entre 0 e 1."""

    return 1.0 / (1.0 + np.exp(-values))


def generate_synthetic_transactions(config: ProblemConfig) -> pd.DataFrame:
    """Gera dados sintéticos com um rótulo futuro de fraude.

    As features representam informações disponíveis no instante da autorização.
    O rótulo é gerado a partir de um risco latente e representa confirmação futura.
    """

    rng = np.random.default_rng(config.random_state)
    timestamps = pd.to_datetime("2026-01-01") + pd.to_timedelta(
        np.sort(rng.integers(0, 180 * 24 * 60, size=config.n_rows)), unit="m"
    )

    data = pd.DataFrame(
        {
            "transaction_id": [f"tx-{index:05d}" for index in range(config.n_rows)],
            "timestamp": timestamps,
            "amount": np.round(rng.lognormal(mean=4.2, sigma=1.0, size=config.n_rows), 2),
            "account_age_days": rng.integers(1, 2_000, size=config.n_rows),
            "transactions_last_24h": rng.poisson(3, size=config.n_rows),
            "distinct_countries_last_7d": rng.integers(1, 5, size=config.n_rows),
            "device_risk_score": np.round(rng.beta(2, 5, size=config.n_rows), 3),
            "is_international": rng.binomial(1, 0.25, size=config.n_rows),
            "prior_chargebacks": rng.poisson(0.15, size=config.n_rows),
            "merchant_risk_score": np.round(rng.beta(2, 4, size=config.n_rows), 3),
        }
    )
    data["hour"] = data["timestamp"].dt.hour

    # Este score é apenas o mecanismo para criar um dataset didático.
    # Em uma aplicação real, o rótulo viria de confirmação posterior.
    latent_risk = (
        -5.0
        + 0.0015 * data["amount"]
        + 0.32 * data["transactions_last_24h"]
        + 1.8 * data["device_risk_score"]
        + 0.75 * data["is_international"]
        + 0.85 * data["prior_chargebacks"]
        + 1.25 * data["merchant_risk_score"]
        + 0.55 * (data["hour"].isin([0, 1, 2, 3])).astype(int)
        - 0.0003 * data["account_age_days"]
    )
    fraud_probability = sigmoid(latent_risk.to_numpy())
    data["fraud_confirmed_within_horizon"] = rng.binomial(1, fraud_probability)

    return data.sort_values("timestamp").reset_index(drop=True)


def temporal_split(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Divide dados por tempo para evitar treinar com o futuro."""

    first_cut = int(len(data) * 0.60)
    second_cut = int(len(data) * 0.80)
    return data.iloc[:first_cut], data.iloc[first_cut:second_cut], data.iloc[second_cut:]


def build_model() -> Pipeline:
    """Cria preprocessing e modelo dentro de um único pipeline."""

    preprocessor = ColumnTransformer(
        transformers=[("numeric", StandardScaler(), FEATURE_COLUMNS)],
        remainder="drop",
    )
    return Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("classifier", LogisticRegression(max_iter=1_000, random_state=42)),
        ]
    )


def rule_baseline(data: pd.DataFrame) -> np.ndarray:
    """Regra manual que representa uma solução anterior ao ML."""

    return (
        (data["amount"] >= 600)
        | (data["device_risk_score"] >= 0.80)
        | (data["prior_chargebacks"] >= 1)
    ).astype(int).to_numpy()


def expected_cost(
    y_true: np.ndarray,
    predictions: np.ndarray,
    false_positive_cost: float,
    false_negative_cost: float,
) -> float:
    """Calcula um custo simples para orientar a política de decisão."""

    false_positives = ((predictions == 1) & (y_true == 0)).sum()
    false_negatives = ((predictions == 0) & (y_true == 1)).sum()
    return float(
        false_positives * false_positive_cost
        + false_negatives * false_negative_cost
    )


def choose_threshold(
    y_true: np.ndarray,
    probabilities: np.ndarray,
    config: ProblemConfig,
) -> tuple[float, float]:
    """Escolhe threshold usando somente a validação e os custos definidos."""

    best_threshold = 0.5
    best_cost = float("inf")
    for threshold in np.linspace(0.05, 0.95, 181):
        predictions = (probabilities >= threshold).astype(int)
        cost = expected_cost(
            y_true,
            predictions,
            config.false_positive_cost,
            config.false_negative_cost,
        )
        if cost < best_cost:
            best_threshold = float(threshold)
            best_cost = cost
    return best_threshold, best_cost


def apply_guardrail(
    data: pd.DataFrame,
    model_predictions: np.ndarray,
    config: ProblemConfig,
) -> tuple[np.ndarray, int]:
    """Aplica uma política de revisão obrigatória após a previsão.

    O guardrail não altera o modelo. Ele altera a decisão operacional final.
    """

    mandatory_review = data["amount"].to_numpy() >= config.high_value_review_limit
    final_decisions = np.where(mandatory_review | (model_predictions == 1), 1, 0)
    return final_decisions.astype(int), int(mandatory_review.sum())


def print_problem_formulation(config: ProblemConfig) -> None:
    """Exibe a formulação antes de executar o experimento."""

    print("\n=== FORMULAÇÃO DO PROBLEMA ===")
    print("Objetivo de negócio: reduzir perdas sem bloquear excessivamente clientes legítimos.")
    print("Unidade: uma transação.")
    print("Momento: antes da autorização.")
    print("Alvo: fraude confirmada posteriormente.")
    print(f"Horizonte: {config.fraud_confirmation_horizon_days} dias.")
    print("Saída: probabilidade de fraude.")
    print("Decisão: aprovar ou enviar para revisão.")
    print(
        "Guardrail: revisão obrigatória para valor >= "
        f"R$ {config.high_value_review_limit:,.2f}."
    )


def evaluate(
    name: str,
    y_true: np.ndarray,
    predictions: np.ndarray,
    probabilities: np.ndarray | None,
    config: ProblemConfig,
) -> None:
    """Exibe métricas técnicas e custo da política."""

    print(f"\n=== AVALIAÇÃO: {name} ===")
    print("Matriz de confusão [linhas=real, colunas=predito]:")
    print(confusion_matrix(y_true, predictions))
    print(f"Precision: {precision_score(y_true, predictions, zero_division=0):.3f}")
    print(f"Recall:    {recall_score(y_true, predictions, zero_division=0):.3f}")
    if probabilities is not None:
        print(f"ROC-AUC:   {roc_auc_score(y_true, probabilities):.3f}")
    print(
        "Custo estimado: "
        f"{expected_cost(y_true, predictions, config.false_positive_cost, config.false_negative_cost):.2f}"
    )
    print("\nRelatório:")
    print(classification_report(y_true, predictions, target_names=["normal", "suspeita"], zero_division=0))


def main() -> None:
    config = ProblemConfig()
    print_problem_formulation(config)

    data = generate_synthetic_transactions(config)
    train, validation, test = temporal_split(data)
    target = "fraud_confirmed_within_horizon"

    print("\n=== DADOS ===")
    print(f"Total: {len(data)} | treino: {len(train)} | validação: {len(validation)} | teste: {len(test)}")
    print(f"Fraudes no total: {data[target].mean():.2%}")
    print(f"Período de treino: {train['timestamp'].min()} até {train['timestamp'].max()}")
    print(f"Período de teste:  {test['timestamp'].min()} até {test['timestamp'].max()}")

    baseline_validation = rule_baseline(validation)
    baseline_test = rule_baseline(test)
    evaluate(
        "baseline: regra manual",
        validation[target].to_numpy(),
        baseline_validation,
        None,
        config,
    )

    model = build_model()
    model.fit(train[FEATURE_COLUMNS], train[target])

    validation_probabilities = model.predict_proba(validation[FEATURE_COLUMNS])[:, 1]
    threshold, validation_cost = choose_threshold(
        validation[target].to_numpy(), validation_probabilities, config
    )
    print(f"\nThreshold escolhido na validação: {threshold:.3f}")
    print(f"Custo de validação no threshold escolhido: {validation_cost:.2f}")

    test_probabilities = model.predict_proba(test[FEATURE_COLUMNS])[:, 1]
    test_model_predictions = (test_probabilities >= threshold).astype(int)
    evaluate(
        "modelo sem guardrail",
        test[target].to_numpy(),
        test_model_predictions,
        test_probabilities,
        config,
    )
    evaluate("baseline: regra manual no teste", test[target].to_numpy(), baseline_test, None, config)

    final_decisions, mandatory_review_count = apply_guardrail(
        test, test_model_predictions, config
    )
    print(f"\nRevisões obrigatórias pelo guardrail: {mandatory_review_count}")
    evaluate(
        "modelo + guardrail de alto valor",
        test[target].to_numpy(),
        final_decisions,
        test_probabilities,
        config,
    )

    result = test[["transaction_id", "timestamp", "amount"]].copy()
    result["fraud_probability"] = np.round(test_probabilities, 3)
    result["model_decision"] = np.where(test_model_predictions == 1, "REVISAR", "APROVAR")
    result["final_decision"] = np.where(final_decisions == 1, "REVISAR", "APROVAR")
    print("\n=== EXEMPLOS DE DECISÃO ===")
    print(result.sort_values("fraud_probability", ascending=False).head(10).to_string(index=False))

    output_path = Path(__file__).with_name("decisoes_teste.csv")
    result.to_csv(output_path, index=False)
    print(f"\nArquivo de decisões salvo em: {output_path}")


if __name__ == "__main__":
    main()
