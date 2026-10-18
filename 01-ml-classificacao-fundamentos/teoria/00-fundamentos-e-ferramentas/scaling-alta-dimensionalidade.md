# Scaling com escalas muito diferentes e muitas dimensões

## 1. Escala diferente não é o mesmo que muitas dimensões

Considere colunas com estes intervalos:

| feature | intervalo |
|---|---:|
| idade | 1 a 10 |
| nota | 0 a 20 |
| renda | 0 a 100.000 |
| patrimônio | 0 a 100.000.000 |
| faturamento | 0 a 1.000.000.000.000 |

O problema imediato é que as colunas estão em unidades e magnitudes diferentes. Muitos algoritmos usam distância ou gradiente. Sem tratamento, uma feature que chega a 1 bilhão pode dominar uma feature que chega a 10.

## 2. StandardScaler trata cada coluna separadamente

O StandardScaler transforma cada coluna j usando:

z_j = (x_j - media_j) / desvio_j

Cada feature possui sua própria média e seu próprio desvio padrão. Portanto, uma coluna de renda e uma coluna de faturamento não são divididas pelo mesmo número.

Depois da transformação, as colunas ficam geralmente com média próxima de 0 e desvio padrão próximo de 1.

O ponto importante é: o valor original deixa de dominar o cálculo apenas por estar em uma unidade maior.

## 3. O problema dos outliers

O StandardScaler usa média e desvio padrão. Valores extremos podem influenciar muito os dois.

Exemplo:

salários = [3000, 3500, 4000, 4500, 5000, 1000000]

O valor de 1.000.000 pode aumentar a média e o desvio padrão, comprimindo a maioria das observações.

### RobustScaler

Usa mediana e intervalo interquartil:

z = (x - mediana) / IQR

É mais resistente a outliers.

### Transformação logarítmica

Para valores positivos e muito assimétricos:

x_novo = log(1 + x)

Em Python:

    X["faturamento_log"] = np.log1p(X["faturamento"])

Exemplo aproximado:

1.000 -> log1p(1000) aproximadamente 6,91
1.000.000 -> log1p(1000000) aproximadamente 13,82
1.000.000.000 -> log1p(1000000000) aproximadamente 20,72

A transformação reduz a diferença entre ordens de grandeza.

## 4. Valores monetários exigem interpretação de negócio

Antes de transformar faturamento ou patrimônio, pergunte:

- o valor é sempre positivo?
- zero tem significado?
- valores negativos existem?
- valores extremos são erros ou clientes legítimos?
- a relação esperada é aditiva ou multiplicativa?
- o modelo precisa interpretar o coeficiente na unidade original?

Não devemos aplicar transformação apenas para deixar os números menores. A decisão depende do domínio.

## 5. Qual scaler escolher?

| Situação | Opção inicial |
|---|---|
| dados aproximadamente simétricos | StandardScaler |
| muitos outliers | RobustScaler |
| valores positivos muito assimétricos | log1p + StandardScaler |
| limites conhecidos, como porcentagem | MinMaxScaler |
| dados esparsos | StandardScaler com cuidado ou MaxAbsScaler |
| árvores de decisão | scaling geralmente dispensável |

## 6. Exemplo com ColumnTransformer

Podemos aplicar tratamentos diferentes por grupo de colunas:

    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler, RobustScaler
    from sklearn.impute import SimpleImputer

    normal_columns = ["idade", "nota"]
    monetary_columns = ["renda", "patrimonio", "faturamento"]

    normal_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    monetary_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler())
    ])

    preprocessor = ColumnTransformer([
        ("normal", normal_pipeline, normal_columns),
        ("monetary", monetary_pipeline, monetary_columns)
    ])

Se decidirmos aplicar logaritmo, podemos criar features logarítmicas antes ou usar FunctionTransformer dentro da pipeline.

## 7. E quando existem muitas dimensões?

Muitas dimensões podem causar outro problema: a maldição da dimensionalidade.

À medida que o número de features cresce:

- os dados ficam mais esparsos no espaço;
- distâncias entre pontos podem ficar menos informativas;
- aumenta o risco de overfitting;
- treinamento e armazenamento podem ficar mais caros;
- features podem ser redundantes ou irrelevantes.

Scaling não resolve sozinho a maldição da dimensionalidade. Ele apenas evita que unidades diferentes distorçam determinadas operações.

Possíveis estratégias:

- remover features irrelevantes;
- usar regularização, como Ridge ou Lasso;
- eliminar features redundantes;
- usar seleção de features;
- aplicar PCA quando fizer sentido;
- usar modelos adequados à alta dimensionalidade;
- monitorar custo computacional e memória.

## 8. Cuidado com dados esparsos

One-hot encoding pode criar milhares de colunas, sendo que cada linha possui poucos valores 1. Transformar uma matriz esparsa em uma matriz densa pode consumir muita memória.

Em determinadas situações, o StandardScaler deve preservar a esparsidade:

    StandardScaler(with_mean=False)

Outra opção é MaxAbsScaler, que preserva zeros e a estrutura esparsa.

## 9. Regra contra vazamento

As estatísticas de scaling devem ser aprendidas apenas no treino:

    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

Nunca calcule média, mediana, quantis ou limites usando treino e teste juntos.

## Resumo

- Escalas diferentes por coluna são tratadas individualmente.
- StandardScaler funciona mesmo quando uma coluna vai até 10 e outra até 1 trilhão.
- Outliers podem tornar média e desvio padrão pouco representativos.
- RobustScaler é útil com outliers.
- log1p é útil para valores positivos e muito assimétricos.
- Muitas dimensões são um problema diferente: a maldição da dimensionalidade.
- Em one-hot de alta cardinalidade, preserve a esparsidade.
- A escolha final depende do algoritmo, da distribuição, dos outliers, do significado de negócio e da memória.

## Fonte principal

Documentação do scikit-learn sobre pré-processamento: https://scikit-learn.org/stable/modules/preprocessing.html

