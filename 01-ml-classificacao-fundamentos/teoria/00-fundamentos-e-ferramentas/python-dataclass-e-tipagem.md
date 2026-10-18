# Python: `dataclass` e tipagem

## `@dataclass`

`@dataclass` transforma uma classe principalmente orientada a dados em uma classe com métodos gerados automaticamente, como `__init__`, `__repr__` e `__eq__`.

```python
from dataclasses import dataclass


@dataclass
class Example:
    name: str
    value: float
```

As anotações ajudam documentação, IDEs e verificadores estáticos, mas não validam os valores durante a execução. Para validação em runtime, use verificações explícitas, `__post_init__` ou uma biblioteca de validação.

`frozen=True` impede atribuições aos campos e é útil para configurações e objetos que devem ser tratados como somente leitura.

## Aplicação em ML

Dataclasses são adequadas para configurações, resultados de avaliação e contratos internos do pipeline. Funções simples continuam sendo preferíveis para transformações simples.

Fonte: https://docs.python.org/3/library/dataclasses.html
