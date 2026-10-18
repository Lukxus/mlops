# Ambientes virtuais e PyCharm

O ambiente virtual deve ser criado no nível de cada projeto principal, e não no nível de cada script ou biblioteca.

```text
MLOPS/
├── 01-ml-classificacao-fundamentos/
│   └── .venv/
└── 02-outro-projeto/
    └── .venv/
```

Todos os scripts dentro de `01-ml-classificacao-fundamentos` compartilham o mesmo `.venv`. Outro projeto usa outro ambiente para evitar conflitos de versões.

No PyCharm, cada configuração de execução deve apontar para:

- o script específico que será executado;
- o `.venv` do projeto ao qual o script pertence;
- o diretório de trabalho do projeto.

O diretório aberto no PyCharm pode ser a raiz geral `MLOPS`, enquanto o diretório de trabalho e o interpretador podem ser específicos do projeto.
