"""Primeiro contato com uma pipeline pré-treinada da Hugging Face.

Este exemplo exige transformers, PyTorch e acesso à internet na primeira execução,
pois o modelo será baixado do Hub.
"""

from transformers import pipeline


def main() -> None:
    classifier = pipeline("sentiment-analysis")
    result = classifier("Estou aprendendo Machine Learning.")
    print(result)


if __name__ == "__main__":
    main()
