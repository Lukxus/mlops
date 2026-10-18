# 00 — Fundamentos e ferramentas

Esta etapa existe para revisar as ferramentas antes de usá-las nos projetos de regressão. O objetivo não é estudar cada biblioteca inteira, mas entender o papel de cada uma no ciclo de Machine Learning.

Para abrir um chat dedicado a esta atividade, use o [contexto do agente](./CONTEXTO_DO_AGENTE.md).

## Ordem recomendada

1. Python para ML
2. NumPy
3. Pandas
4. Matemática e estatística com SciPy
5. Visualização com Matplotlib e Seaborn
6. Scikit-learn
7. PyTorch
8. Hugging Face
9. Jupyter e ambiente de desenvolvimento

## Pergunta central

Para cada ferramenta, responder:

> Que problema ela resolve, qual é o objeto principal que ela manipula, em que etapa do pipeline ela aparece e quando eu não deveria usá-la?

## O que revisar

### Python para ML

- funções, módulos e pacotes;
- listas, dicionários, tuplas e conjuntos;
- compreensão de listas;
- exceções;
- leitura e escrita de arquivos;
- ambientes virtuais;
- tipagem e organização de código;
- testes básicos.

### NumPy

- arrays e dimensões;
- shape, dtype e broadcasting;
- indexação e slicing;
- operações vetorizadas;
- média, variância e soma;
- multiplicação elemento a elemento versus produto matricial;
- geração de dados sintéticos.

### Pandas

- Series e DataFrame;
- seleção e filtragem;
- tipos de dados;
- valores ausentes;
- agrupamento e agregação;
- merge e join;
- leitura de CSV e Parquet;
- ordenação temporal;
- risco de leakage durante transformações.

### SciPy

- estatística descritiva;
- distribuições de probabilidade;
- correlação;
- testes estatísticos básicos;
- funções de otimização;
- quando usar SciPy em vez de implementar uma fórmula manualmente.

### Matplotlib e Seaborn

- gráfico de dispersão;
- linha de regressão;
- histograma;
- boxplot;
- gráfico de resíduos;
- heatmap de correlação;
- escolha correta de eixos, escalas e legendas.

### Scikit-learn

- divisão treino/teste;
- estimators, transformers e pipelines;
- `fit`, `transform` e `predict`;
- métricas;
- validação cruzada;
- busca de hiperparâmetros;
- pré-processamento;
- modelos lineares, árvores e ensembles;
- persistência e reprodutibilidade.

### PyTorch

- tensor e shape;
- operações em tensores;
- dataset e dataloader;
- função de perda;
- gradiente e autograd;
- modelo, optimizer e loop de treinamento;
- diferença entre treinamento manual e APIs de alto nível.

PyTorch não será necessário para os primeiros projetos de regressão clássica. Ele entra para entender a base de modelos treinados por gradiente e preparar a transição para redes neurais.

### Hugging Face

- modelos e tokenizers;
- datasets;
- model hub;
- inferência versus fine-tuning;
- pipelines prontas;
- limites de usar modelos pré-treinados sem compreender dados, métricas e avaliação.

Hugging Face será uma revisão de repertório para etapas futuras. Não será prioridade antes de consolidar regressão, classificação e avaliação.

### Jupyter e ambiente

- notebooks versus scripts;
- kernels e ambientes virtuais;
- instalação e versionamento de dependências;
- organização de experimentos;
- execução reprodutível;
- conversão de notebook em código de projeto.

## Entrega desta etapa

Criar pequenos notebooks independentes, um por ferramenta, sempre respondendo:

1. qual problema a ferramenta resolve;
2. qual é seu objeto principal;
3. qual é a entrada e a saída;
4. como ela aparece em um pipeline de ML;
5. quais erros de uso são comuns.

## Como executar

Instale as dependências em um ambiente virtual antes de executar os exemplos:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Depois, execute cada `main.py` a partir da respectiva pasta.

Os scripts já foram verificados quanto à sintaxe. As bibliotecas ainda precisam ser instaladas neste ambiente antes da execução completa.

## Regra de prioridade

Para os projetos atuais, a prioridade é:

```text
Python → NumPy → Pandas → visualização → Scikit-learn
```

SciPy entra como apoio matemático e estatístico. PyTorch e Hugging Face serão estudados conceitualmente agora e praticados com mais profundidade depois.
