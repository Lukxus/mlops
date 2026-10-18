"""Checklist simples de reprodutibilidade do ambiente."""

import platform
import sys


def main() -> None:
    print("Python:", sys.version)
    print("Sistema:", platform.platform())
    print("Executável:", sys.executable)
    print("\nPróximo passo: registrar dependências em requirements.txt ou pyproject.toml.")


if __name__ == "__main__":
    main()
