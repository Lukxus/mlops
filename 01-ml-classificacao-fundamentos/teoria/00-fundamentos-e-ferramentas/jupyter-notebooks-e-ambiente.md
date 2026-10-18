# Jupyter, notebooks e ambiente do projeto

## Estado atual

O projeto já possui:

- a pasta `aplicacao/00-fundamentos-e-ferramentas/09-jupyter-e-ambiente/`;
- um `main.py` que imprime versão do Python, sistema operacional e executável usado;
- um `README.md` com a entrega esperada;
- `jupyter` e `ipykernel` no `aplicacao/requirements.txt`;
- os pacotes Jupyter instalados no `.venv` do projeto.

O projeto ainda não possui arquivos `.ipynb`. Portanto, a configuração chamada `Jupyter e ambiente` executa apenas o `main.py` de verificação; ela não inicia um servidor Jupyter.

## Notebook versus script

Um script `.py` é um arquivo executável linear, adequado para código organizado, testes e automação.

Um notebook `.ipynb` combina células de código, resultados, gráficos e texto. É útil para exploração, visualização e comunicação de experimentos.

O notebook não substitui automaticamente o script. A prática recomendada é explorar no notebook e, quando o fluxo estiver compreendido, mover lógica reutilizável para módulos ou scripts testáveis.

## Organização recomendada

```text
01-ml-classificacao-fundamentos/
├── notebooks/
├── aplicacao/
│   └── 00-fundamentos-e-ferramentas/
└── .venv/
```

## Iniciar o Jupyter

Com o ambiente ativado e na raiz do projeto:

```powershell
python -m jupyter lab
```

O navegador abrirá a interface do Jupyter usando o Python do `.venv`.
