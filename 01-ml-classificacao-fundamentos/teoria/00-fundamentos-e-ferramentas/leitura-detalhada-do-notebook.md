# Leitura detalhada do primeiro notebook

## 1. Por que são estatísticas do alvo de regressão?

`diabetes_df["target"]` seleciona apenas a coluna que o modelo deve prever. Na base Diabetes, esse alvo é um valor numérico contínuo, portanto o problema é de regressão. `describe()` resume contagem, média, desvio padrão, mínimo, quartis e máximo.

## 2. Histograma do alvo

As barras mostram quantas observações caem em cada intervalo de valores do alvo. A curva do Seaborn é uma estimativa suavizada da densidade. O gráfico ajuda a observar concentração, assimetria, caudas e possíveis valores extremos, mas não prova causalidade nem qualidade do modelo.

## 3. Heatmap

O heatmap mostra a correlação de Pearson entre variáveis. Valores próximos de `1` indicam associação linear positiva; valores próximos de `-1`, associação linear negativa; valores próximos de `0`, pouca associação linear. Correlação não implica causalidade. Correlações altas entre features podem indicar redundância ou multicolinearidade.

Na base de câncer, `target` é uma classe codificada como número. O sinal depende da codificação das classes; a associação não deve ser interpretada como causalidade.

## 4. Pré-processamento, processamento e fine-tuning

Processamento é o termo geral para manipular dados. Pré-processamento é o conjunto de transformações feitas antes da entrada no modelo, como imputação, encoding, scaling e seleção de features. Essas transformações devem ser aprendidas no treino e aplicadas ao teste e à produção.

Fine-tuning é adaptar um modelo pré-treinado a uma tarefa ou domínio específico. Não é o mesmo que ajustar hiperparâmetros: fine-tuning altera parâmetros aprendidos do modelo; tuning procura configurações do treinamento ou do algoritmo.

## 5. Scaling

Scaling coloca features em escalas comparáveis. Na padronização:

```text
z = (x - média_do_treino) / desvio_padrão_do_treino
```

Ele é importante para modelos sensíveis a distância ou magnitude, como regressão logística, Ridge, SVM, k-NN e redes neurais. Árvores geralmente são menos sensíveis à escala.

O scaler deve usar `fit` apenas no treino e `transform` no teste, para evitar leakage.

## 6. `max_iter`

`max_iter=2000` limita o número máximo de iterações do algoritmo otimização da regressão logística. Não significa necessariamente 2000 épocas de uma rede neural. Se o modelo não convergir, pode aparecer um aviso; aumentar o limite pode ajudar, mas também é necessário investigar escala, dados e solver.

## 7. Classification report

- `precision = TP / (TP + FP)`: entre as previsões de uma classe, quantas estavam corretas;
- `recall = TP / (TP + FN)`: entre os casos reais de uma classe, quantos foram encontrados;
- `f1-score`: média harmônica entre precision e recall;
- `support`: quantidade real de exemplos daquela classe no conjunto avaliado.

As métricas são calculadas por classe no formato one-vs-rest. `macro avg` dá o mesmo peso a cada classe; `weighted avg` pondera pelo support.

## 8. Matriz de confusão

Linhas representam a classe real e colunas a classe prevista. Na imagem, os valores são aproximadamente:

```text
real malignant, previsto malignant = 41
real malignant, previsto benign    = 1
real benign, previsto malignant    = 1
real benign, previsto benign       = 71
```

Ela mostra diretamente acertos e tipos de erro. É essencial quando os custos de falso positivo e falso negativo são diferentes.

## 9. Pipeline

```python
ridge_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0)),
])
```

No `fit`, o pipeline ajusta o scaler no treino e depois ajusta o modelo nos dados transformados. No `predict`, transforma dados novos com o scaler já aprendido e chama o modelo. `alpha` controla a força da regularização Ridge.

## 10. Resíduos

O resíduo é:

```text
resíduo = valor_real - previsão
```

Um gráfico de resíduos ajuda a detectar padrão não capturado, heterocedasticidade, outliers e não linearidade. Um bom sinal é uma nuvem sem estrutura clara ao redor de zero. Resíduos não substituem métricas.

## 11. Tensor e treinamento PyTorch

Um tensor é uma estrutura numérica multidimensional. Pode representar escalares, vetores, matrizes ou dados com mais dimensões, e pode ser colocado em CPU ou GPU.

No notebook:

- `StandardScaler` padroniza as features usando somente o treino;
- `torch.tensor(..., dtype=torch.float32)` converte features para tensores adequados à rede;
- `dtype=torch.long` representa índices inteiros das classes;
- `TensorDataset` associa cada linha de features ao seu rótulo;
- `DataLoader` divide os dados em lotes de 32 e embaralha o treino;
- `nn.Linear(n_features, 32)` cria a primeira camada;
- `ReLU` adiciona não linearidade;
- `nn.Linear(32, 2)` produz dois logits, um por classe;
- `CrossEntropyLoss` compara logits com os rótulos inteiros;
- `Adam` atualiza os pesos usando os gradientes;
- `loss.backward()` calcula gradientes;
- `optimizer.step()` altera os parâmetros;
- `train()` ativa o modo de treinamento;
- `eval()` ativa o modo de avaliação;
- `no_grad()` evita calcular gradientes durante a inferência;
- `argmax(dim=1)` escolhe a classe com maior logit.

O código atual treina em CPU. Para usar CUDA, modelo e lotes precisam ser movidos para o mesmo dispositivo.
