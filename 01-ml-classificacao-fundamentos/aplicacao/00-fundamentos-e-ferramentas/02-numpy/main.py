"""Revisão de arrays, vetorização e erro com NumPy."""

import numpy as np


def main() -> None:
    features = np.array([1.0, 2.0, 3.0, 4.0])
    target = np.array([2.0, 3.0, 5.0, 7.0])

    # Modelo simples: y_hat = 1.5x + 0.5
    predictions = 1.5 * features + 0.5
    errors = target - predictions
    mse = np.mean(errors**2)

    print("shape:", features.shape)
    print("previsões:", predictions)
    print("erros:", errors)
    print("MSE:", mse)


if __name__ == "__main__":
    main()
