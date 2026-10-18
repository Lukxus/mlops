# Conda e Miniconda

## Conda

Conda é um gerenciador de ambientes, pacotes e dependências. Ele pode criar ambientes isolados com diferentes versões de Python e também gerenciar pacotes e dependências nativas, inclusive de outras linguagens.

Exemplo:

```powershell
conda create -n ml-fundamentos python=3.13
conda activate ml-fundamentos
conda install numpy pandas scikit-learn
```

Um ambiente conda pode ser exportado para um arquivo `environment.yml` e recriado em outra máquina.

## Miniconda

Miniconda é um instalador mínimo que inclui o conda, Python e um pequeno conjunto de pacotes. Os demais pacotes são instalados conforme a necessidade.

Ele não é outro gerenciador: é uma forma leve de instalar o conda.

## Anaconda

Anaconda Distribution é uma distribuição completa que inclui conda e muitos pacotes de ciência de dados, além de ferramentas como Jupyter. Ocupa mais espaço e instala mais componentes inicialmente.

## Comparação com `venv` e `pip`

| Abordagem | Papel |
|---|---|
| `venv` | Isola um ambiente Python |
| `pip` | Instala pacotes Python do PyPI |
| `conda` | Cria ambientes e gerencia pacotes Python e dependências nativas |
| Miniconda | Instalação mínima que fornece o conda |

Conda e `venv` resolvem o isolamento de ambientes, mas têm ecossistemas e mecanismos de resolução diferentes. Não é necessário usar os dois no mesmo projeto sem uma razão específica.

## Decisão para este projeto

O projeto atual já usa um `.venv` funcional com `requirements.txt`. Portanto, a recomendação é continuar com `venv` e `pip` nesta etapa, evitando trocar a ferramenta no meio do estudo.

Conda pode ser interessante em projetos futuros com dependências nativas difíceis, múltiplas versões de Python, ambientes científicos mais complexos ou necessidades específicas de distribuição.

Fontes:

- https://docs.conda.io/projects/conda/en/stable/user-guide/install/
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://www.anaconda.com/download
