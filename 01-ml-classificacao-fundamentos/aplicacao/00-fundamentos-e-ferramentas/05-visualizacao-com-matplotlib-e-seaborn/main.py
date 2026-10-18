"""Cria gráficos básicos para analisar uma relação de regressão."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    data = pd.DataFrame(
        {"hours": [1, 2, 3, 4, 5], "score": [2, 3, 5, 7, 8]}
    )

    sns.set_theme(style="whitegrid")
    figure, axis = plt.subplots(figsize=(7, 4))
    sns.regplot(data=data, x="hours", y="score", ax=axis, ci=None)
    axis.set_title("Relação entre horas de estudo e nota")
    axis.set_xlabel("Horas estudadas")
    axis.set_ylabel("Nota")
    figure.tight_layout()

    output = Path(__file__).with_name("relacao-horas-nota.png")
    figure.savefig(output, dpi=150)
    print(f"Gráfico salvo em: {output}")


if __name__ == "__main__":
    main()
