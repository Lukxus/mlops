# Encoding e scaling no pré-processamento

## Visão geral

Um CSV bruto normalmente contém valores em formatos diferentes:

| idade | cidade | renda | cliente_ativo |
|---:|---|---:|---|
| 31 | São Paulo | 5000 | sim |
| 45 | Recife | 8000 | não |
| vazio | Curitiba | 6200 | sim |

Um modelo matemático não entende diretamente textos como São Paulo ou sim. Ele precisa receber uma matriz numérica consistente.

O fluxo comum é:

CSV bruto
↓
tratamento de nulos
↓
encoding
↓
scaling
↓
modelo

Esse fluxo é uma simplificação didática. Na prática, o tratamento pode incluir validação de tipos, remoção de duplicidades e criação de features.

## 1. Tratamento de nulos

Valores ausentes precisam ser tratados porque muitos modelos não aceitam valores vazios.

Exemplos:

- idade ausente: substituir pela mediana;
- cidade ausente: substituir por uma categoria como desconhecido;
- linha com informação essencial ausente: remover, se fizer sentido no domínio.

Os valores usados para preencher nulos devem ser calculados no treino e depois aplicados ao teste. Se calcularmos a mediana usando treino e teste juntos, o teste influencia o treinamento.

## 2. Encoding

Encoding transforma categorias em números.

### Label encoding

Exemplo:

pequeno -> 0
medio -> 1
grande -> 2

Esse encoding pode ser adequado quando existe uma ordem real. Porém, para cidades, atribuir São Paulo -> 0, Recife -> 1 e Curitiba -> 2 cria uma ordem falsa. O modelo poderia interpretar que Curitiba é maior que Recife.

### One-hot encoding

O one-hot encoding cria uma coluna para cada categoria:

| cidade | cidade_Curitiba | cidade_Recife | cidade_São_Paulo |
|---|---:|---:|---:|
| Curitiba | 1 | 0 | 0 |
| Recife | 0 | 1 | 0 |
| São Paulo | 0 | 0 | 1 |

Não existe uma ordem artificial entre as cidades.

Em scikit-learn:

    from sklearn.preprocessing import OneHotEncoder
    encoder = OneHotEncoder(handle_unknown="ignore")

handle_unknown="ignore" evita que uma categoria nova em produção quebre a inferência.

### Encoding ordinal

Para uma categoria com ordem real:

baixo -> 0
medio -> 1
alto -> 2

podemos usar valores numéricos, desde que essa ordem faça sentido no domínio.

## 3. Scaling

Scaling coloca variáveis numéricas em escalas comparáveis.

Imagine:

idade: 18 a 80
salário: 2.000 a 30.000

O salário tem valores numericamente maiores. Em alguns algoritmos, ele pode dominar o cálculo simplesmente por estar em uma escala maior.

### StandardScaler

A padronização calcula:

z = (x - média) / desvio padrão

Exemplo:

idade = 40
média = 30
desvio padrão = 10

z = (40 - 30) / 10 = 1

Isso significa que a idade está um desvio padrão acima da média.

### MinMaxScaler

Outra opção é colocar os valores em um intervalo, geralmente de 0 a 1:

x_novo = (x - mínimo) / (máximo - mínimo)

Exemplo:

x = 70
mínimo = 50
máximo = 100

x_novo = (70 - 50) / (100 - 50) = 0,4

## 4. Quando scaling é importante?

Scaling costuma ser importante para:

- regressão logística;
- Ridge e Lasso;
- SVM;
- KNN;
- K-Means;
- redes neurais;
- métodos baseados em gradiente.

A distância entre pontos e o tamanho dos gradientes dependem da escala.

Exemplo em KNN:

idade: 30 versus 31       diferença = 1
renda: 3000 versus 9000   diferença = 6000

Sem scaling, a renda tende a dominar a distância.

Scaling geralmente é menos necessário para árvores de decisão, Random Forest e Gradient Boosting baseado em árvores. Esses modelos fazem divisões por limiares e não dependem da distância euclidiana da mesma maneira.

## 5. Ordem correta em Machine Learning

O fluxo correto é:

1. separar treino e teste;
2. aprender imputação, encoding e scaling no treino;
3. aplicar as mesmas transformações no teste;
4. treinar o modelo;
5. avaliar no teste.

Exemplo:

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=2000))
    ])

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

Para dados mistos, use ColumnTransformer para aplicar tratamentos diferentes às colunas numéricas e categóricas.

## 6. O ponto mais importante: data leakage

Não faça o scaling de todo o dataset antes de separar treino e teste:

    X_scaled = StandardScaler().fit_transform(X)
    X_train, X_test = train_test_split(X_scaled)

Nesse caso, a média e o desvio padrão do teste participaram do scaling. Isso permite que informações do teste contaminem o treinamento.

O correto é deixar a Pipeline aprender as transformações apenas no treino:

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

O Pipeline chama fit apenas no treino e reutiliza a transformação aprendida no teste.

## Resumo

- Nulos: tratam ausência de valores.
- Encoding: transforma categorias em números.
- Scaling: coloca variáveis numéricas em escalas comparáveis.
- Modelo: aprende padrões usando a matriz preparada.
- Pipeline: empacota as transformações e ajuda a evitar inconsistências e vazamento.

Encoding e scaling não melhoram automaticamente os dados. Eles tornam os dados compatíveis com o modelo e com a matemática do algoritmo.

## Fonte principal

Documentação do scikit-learn sobre composição de estimadores e pipelines: https://scikit-learn.org/stable/modules/compose.html

