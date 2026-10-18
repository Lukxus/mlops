"""Revisão de estatística e otimização com SciPy."""

import numpy as np
from scipy import optimize, stats


def main() -> None:
    values = np.array([10.0, 12.0, 13.0, 15.0, 20.0])
    print("Média:", values.mean())
    print("Desvio padrão:", values.std())
    print("Mediana:", np.median(values))
    print("Correlação com a posição:", stats.pearsonr(np.arange(len(values)), values).statistic)

    # Encontrar o ponto mínimo de uma função simples.
    result = optimize.minimize_scalar(lambda x: (x - 3) ** 2 + 1)
    print("Mínimo aproximado:", result.x)


if __name__ == "__main__":
    main()
