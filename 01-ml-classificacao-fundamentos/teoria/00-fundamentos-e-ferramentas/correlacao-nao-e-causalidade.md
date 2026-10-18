# Correlação não é causalidade

## 1. O que o exemplo Diabetes está prevendo?

No notebook existem dois datasets diferentes:

- **Diabetes**: regressão. Cada linha possui 10 medidas clínicas de um paciente e um target numérico associado à progressão da doença. O objetivo é aprender uma função que estime esse valor: y estimado = f(X). O target não representa tamanho de tumor, não é percentual de crescimento e não é uma coluna de datas.
- **Breast Cancer Wisconsin**: classificação. O alvo indica uma classe, como malignant ou benign.

A documentação do scikit-learn descreve o primeiro como diabetes dataset (regression) e o exemplo oficial o usa para prever progressão da doença.

### Isso é série temporal?

Não automaticamente. Uma série temporal exige ordem temporal relevante e normalmente várias medições ao longo do tempo, por exemplo paciente, data, glicose, peso e progressão. O dataset usado no notebook não fornece uma sequência completa de medições por paciente. Ele é tratado como dado tabular: X -> y.

Se a pergunta fosse “qual será a progressão deste paciente nos próximos 3 meses?”, ainda poderíamos fazer regressão supervisionada com um único horizonte. Para estudar trajetória, tendência e previsão de vários passos, precisaríamos de dados longitudinais, identificador do paciente, datas, divisão cronológica e técnicas de séries temporais ou modelos longitudinais.

## 2. Correlação

A correlação de Pearson mede associação linear:

rho(X,Y) = Cov(X,Y) / (sigma_X sigma_Y)

Cov(X,Y) = E[(X-E[X])(Y-E[Y])]

- rho próximo de 1: associação linear positiva forte;
- rho próximo de -1: associação linear negativa forte;
- rho próximo de 0: pouca associação linear.

Exemplo: X=[1,2,3] e Y=[2,4,6]. A associação é perfeitamente positiva, rho=1. Isso ainda não prova que mudar X causaria mudança em Y.

## 3. Causalidade

Causalidade pergunta o que aconteceria se fizéssemos uma intervenção.

Para um tratamento binário A:

ATE = E[Y(1)-Y(0)]

Y(1) é o resultado potencial se a unidade receber o tratamento; Y(0) é o resultado potencial sem tratamento.

Na notação de intervenção, E[Y | do(X=x)] significa a média de Y quando forçamos X a assumir x. Isso é diferente de observar pessoas que naturalmente têm X=x: E[Y | X=x].

## 4. Demonstração matemática: correlação sem efeito causal

Considere:

Z ~ N(0,1)
X = Z + epsilon_X
Y = Z + epsilon_Y

Suponha ruídos independentes, média 0 e variância 1. O grafo é X <- Z -> Y. Não existe X -> Y.

Cov(X,Y) = Cov(Z+epsilon_X, Z+epsilon_Y) = Var(Z) = 1

Var(X)=2 e Var(Y)=2. Logo:

rho(X,Y) = 1 / (sqrt(2) sqrt(2)) = 1/2 = 0.5

A regressão observacional também encontra:

beta = Cov(X,Y)/Var(X) = 1/2 = 0.5

Mas na intervenção do(X=x), a equação de X é substituída por uma constante. Y continua igual a Z + epsilon_Y. Portanto:

E[Y | do(X=x)] = 0

para qualquer x, e o efeito causal é 0. A associação de 0.5 foi criada pelo confundidor Z.

## 5. Como lidar com isso?

Primeiro defina a pergunta:

- **Predição:** dadas estas características, qual será o alvo?
- **Causalidade:** se eu mudar X, o resultado mudará?

Para análise causal:

1. desenhe um DAG, um grafo de hipóteses causais;
2. procure confundidores, que influenciam X e Y;
3. não controle automaticamente tudo: mediadores e colisores podem introduzir viés;
4. prefira experimento randomizado quando possível;
5. em dados observacionais, ajuste por um conjunto válido de confundidores;
6. declare as hipóteses, pois nenhum algoritmo elimina confundimento não medido.

Se Z for um conjunto válido de confundidores, a fórmula de ajuste pela porta de trás é:

E[Y | do(X=x)] = sum_z E[Y | X=x,Z=z] P(Z=z)

Para Z contínuo, a soma vira integral. A ideia é comparar pessoas com valores semelhantes de Z e depois padronizar para a distribuição total.

## 6. O que o heatmap permite dizer?

Ele permite dizer: “estas variáveis estão associadas ao alvo nesta amostra”. Não permite dizer: “esta variável causa a doença”.

No ML preditivo, correlação é útil para conhecer os dados, encontrar redundância, detectar relações lineares, orientar hipóteses e investigar multicolinearidade. Um modelo preditivo pode ser excelente sem ser causal.

## Fontes

- Scikit-learn, documentação do dataset Diabetes: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html
- Exemplo oficial do scikit-learn: https://scikit-learn.org/stable/auto_examples/applications/plot_model_complexity_influence.html
- Hernán e Robins, Causal Inference: What If: https://miguelhernan.org/whatifbook
- PDF de Hernán e Robins: https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf
- Material universitário sobre ajuste pela porta de trás: https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/mci/2026/lec10pearladjustmentformula.pdf

## Fonte principal

Hernán e Robins, Causal Inference: What If: https://miguelhernan.org/whatifbook

