"""Revisão de Python para Machine Learning."""

from dataclasses import dataclass


@dataclass
class Example:
    name: str
    value: float

def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("A lista não pode estar vazia")
    return sum(values) / len(values)


def main() -> None:
    observations = [Example("A", 10.0), Example("B", 20.0), Example("C", 30.0)]
    values = [item.value for item in observations]
    print("Média:", mean(values))


if __name__ == "__main__":
    main()
