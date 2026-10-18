# Python puro, NumPy e Pandas

## Python puro

Listas, dicionários e loops são suficientes para exemplos pequenos, regras específicas e para aprender a lógica do cálculo.

## NumPy

NumPy fornece arrays multidimensionais homogêneos, operações vetorizadas, `shape`, `dtype`, indexação e álgebra numérica. É a base numérica de várias bibliotecas científicas e de Machine Learning.

```python
import numpy as np

features = np.array([1, 2, 3, 4])
predictions = 2 * features + 1
```

## Pandas

Pandas é mais adequado para dados tabulares com nomes de colunas, índices, valores ausentes, filtros, agrupamentos, joins e leitura de arquivos.

```python
summary = data.groupby("service")["latency"].mean()
```

A regra prática é aprender primeiro a operação manualmente e depois usar a biblioteca para expressá-la com eficiência e integrá-la ao pipeline.

Fontes: https://numpy.org/doc/stable/user/absolute_beginners.html e https://pandas.pydata.org/docs/getting_started/overview.html
