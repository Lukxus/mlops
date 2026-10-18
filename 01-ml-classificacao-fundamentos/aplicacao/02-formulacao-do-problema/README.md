# 02 — Aplicação da formulação do problema

Este laboratório transforma a teoria de `teoria/02-formulacao-do-problema` em um exemplo executável.

## Exemplo escolhido

Classificar uma transação como `normal` ou `suspeita` no momento da autorização.

O exemplo é sintético e não representa um sistema antifraude real.

## Formulação

- **Objetivo de negócio:** reduzir perdas com fraude sem bloquear excessivamente clientes legítimos.
- **Unidade de previsão:** uma transação.
- **População:** transações processadas pelo sistema.
- **Momento da previsão:** antes da autorização.
- **Features:** somente informações disponíveis até a autorização.
- **Variável-alvo:** fraude confirmada posteriormente.
- **Horizonte:** confirmação dentro de 30 dias.
- **Saída do modelo:** probabilidade de fraude.
- **Decisão:** aprovar ou enviar para revisão.
- **Guardrail:** transações de valor muito alto são encaminhadas para revisão, mesmo que o modelo fique abaixo do threshold.
- **Baseline:** regra simples baseada em valor e risco do dispositivo.

## O que o código demonstra

1. Geração reprodutível de dados sintéticos.
2. Separação temporal entre treino, validação e teste.
3. Preprocessing dentro de um `Pipeline`.
4. Regressão logística como modelo de classificação.
5. Escolha do threshold usando custo de falso positivo e falso negativo.
6. Comparação com uma regra manual.
7. Aplicação de guardrail na camada de decisão.
8. Avaliação final e exemplos de decisões.

## Como executar no terminal

Na raiz do projeto:

```powershell
python -m pip install -r .\01-ml-classificacao-fundamentos\aplicacao\02-formulacao-do-problema\requirements.txt
python .\01-ml-classificacao-fundamentos\aplicacao\02-formulacao-do-problema\01-transacoes-suspeitas\main.py
```

## Como executar no PyCharm

Foi criada a configuração compartilhada:

`MLOPS/.idea/runConfigurations/01_ml_formulacao_transacoes.xml`

No PyCharm:

1. Selecione `01-ml-classificacao-fundamentos - Formulação - Transações` no seletor de configurações.
2. Confirme que o interpretador aponta para `01-ml-classificacao-fundamentos/.venv/Scripts/python.exe`.
3. Execute com Run ou Debug.

Se o interpretador ainda não tiver as dependências:

```powershell
python -m pip install -r .\01-ml-classificacao-fundamentos\aplicacao\02-formulacao-do-problema\requirements.txt
```

## Limitações didáticas

- Os dados são artificiais.
- A confirmação de fraude é simulada.
- Os custos são hipóteses de demonstração.
- O guardrail é uma política ilustrativa, não uma recomendação antifraude.
- O código não deve ser usado para tomar decisões financeiras reais.
