"""Primeiro modelo de regressão usando scikit-learn."""

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np


def main() -> None:
    dataset = load_diabetes()
    X = dataset.data[:, [2]]  # Uma única feature para manter o exemplo simples.
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Coeficiente:", model.coef_[0])
    print("Intercepto:", model.intercept_)
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))
    print("R²:", r2_score(y_test, predictions))


if __name__ == "__main__":
    main()
