"""Revisão de DataFrame, valores ausentes e agregação com Pandas."""

import pandas as pd


def main() -> None:
    data = pd.DataFrame(
        {
            "service": ["api", "api", "worker", "worker"],
            "requests": [100, 150, 80, 120],
            "latency_ms": [20.0, None, 50.0, 55.0],
        }
    )

    print("Dados originais:\n", data)
    data["latency_ms"] = data["latency_ms"].fillna(data["latency_ms"].median())
    summary = data.groupby("service", as_index=False)["latency_ms"].mean()

    print("\nDados após tratar nulo:\n", data)
    print("\nLatência média por serviço:\n", summary)


if __name__ == "__main__":
    main()
