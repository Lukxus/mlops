# Parâmetros aprendidos e hiperparâmetros

## 1. Ideia central

Um modelo pode ser representado de forma simplificada por:

    y_hat = f(X; theta, lambda)

Onde:

- X são as entradas;
- y_hat é a previsão;
- theta são os parâmetros aprendidos;
- lambda representa hiperparâmetros.

A diferença principal é:

- **parâmetros:** o algoritmo aprende a partir dos dados;
- **hiperparâmetros:** nós configuramos antes do treinamento ou escolhemos por validação.

## 2. Exemplo com uma reta

Considere:

    y_hat = w*x + b

Aqui:

- w é o peso ou inclinação;
- b é o intercepto;
- w e b são parâmetros aprendidos.

Durante o treinamento, o modelo procura valores de w e b que produzam previsões próximas dos valores reais.

Com três pontos:

    x = [1, 2, 3]
    y = [3, 5, 7]

Uma reta adequada é:

    y_hat = 2*x + 1

Nesse caso:

    w = 2
    b = 1

O modelo poderia ter começado com w=0 e b=0, mas aprendeu w=2 e b=1 minimizando o erro.

## 3. O que o treinamento minimiza?

Uma função de perda mede o erro:

    Loss(theta) = erro entre y e f(X; theta)

Para regressão, uma possibilidade é o erro quadrático médio:

    MSE = (1/n) * sum((y_i - y_hat_i)^2)

O treinamento altera theta para reduzir a perda.

Em uma rede neural:

    theta = pesos e vieses de todas as camadas

Em uma regressão linear:

    theta = pesos e intercepto

Em uma regressão logística:

    theta = coeficientes e intercepto

## 4. Onde entram os hiperparâmetros?

Uma representação mais completa é:

    theta_star(lambda) = argmin_theta Loss(theta; lambda)

Isso significa:

> Para uma configuração de hiperparâmetros lambda, encontre os parâmetros theta que minimizam a perda.

Depois:

    y_hat = f(X; theta_star(lambda), lambda)

Os hiperparâmetros alteram o processo, a restrição ou a estrutura do modelo. Eles não são normalmente descobertos diretamente pelo ajuste padrão do modelo.

## 5. learning_rate

Em métodos baseados em gradiente, o modelo atualiza seus parâmetros assim:

    theta_novo = theta_atual - learning_rate * gradiente

O learning_rate controla o tamanho do passo.

### Learning rate pequeno

    learning_rate = 0.001

- atualizações pequenas;
- treinamento mais lento;
- pode exigir muitas épocas;
- tende a ser mais estável.

### Learning rate grande

    learning_rate = 1.0

- atualizações grandes;
- pode treinar mais rapidamente;
- pode ultrapassar o mínimo;
- pode fazer a perda oscilar ou explodir.

O learning_rate não é um peso final aprendido. Ele decide como os pesos serão atualizados.

Exemplo numérico:

    theta_atual = 10
    gradiente = 4

Com learning_rate=0.1:

    theta_novo = 10 - 0.1*4 = 9.6

Com learning_rate=0.01:

    theta_novo = 10 - 0.01*4 = 9.96

O gradiente é o mesmo, mas o passo é diferente.

## 6. alpha em Ridge

Na regressão Ridge, a função objetivo é:

    Loss = MSE + alpha * sum(w_j^2)

Onde:

- MSE mede o erro de previsão;
- w_j são os pesos;
- alpha controla a força da regularização.

Se alpha=0:

    Loss = MSE

O modelo se preocupa apenas em ajustar os dados.

Se alpha for grande:

- pesos grandes ficam mais penalizados;
- o modelo tende a ficar mais simples;
- pode reduzir overfitting;
- se for exagerado, pode causar underfitting.

O alpha é um hiperparâmetro. Os pesos w_j são parâmetros aprendidos.

Em código:

    Ridge(alpha=1.0)

O 1.0 é uma configuração escolhida antes. Depois do fit, os valores aprendidos aparecem em:

    ridge.coef_
    ridge.intercept_

## 7. max_depth em árvores

Uma árvore de decisão aprende regras como:

    renda > 5000?
    idade <= 35?

Os limiares e regras encontrados são parâmetros aprendidos a partir dos dados.

Já max_depth limita a profundidade máxima da árvore:

    DecisionTreeClassifier(max_depth=3)

O max_depth é um hiperparâmetro porque define a capacidade máxima do modelo.

### max_depth pequeno

- árvore simples;
- menor risco de memorizar o treino;
- pode não capturar padrões complexos;
- risco de underfitting.

### max_depth grande

- árvore mais expressiva;
- pode capturar relações complexas;
- maior risco de memorizar ruído;
- risco de overfitting.

Portanto, max_depth não é uma regra aprendida diretamente. Ele restringe quais árvores podem ser construídas.

## 8. Exemplo com regressão logística

A função de decisão pode ser escrita como:

    z = w_1*x_1 + w_2*x_2 + ... + b

    p(y=1|x) = 1 / (1 + exp(-z))

Os parâmetros aprendidos são:

    w_1, w_2, ..., b

Exemplo:

    LogisticRegression(max_iter=2000, C=1.0)

- max_iter é hiperparâmetro do processo de otimização;
- C controla a força inversa da regularização;
- coef_ contém os pesos aprendidos;
- intercept_ contém o intercepto aprendido.

O modelo não aprende automaticamente que max_iter deve ser 2000. Nós definimos esse limite para permitir que o algoritmo encontre uma solução.

## 9. max_iter não é igual a parâmetro do modelo

Em:

    LogisticRegression(max_iter=2000)

max_iter significa o número máximo de iterações permitidas pelo algoritmo de otimização.

Ele não representa uma característica da relação entre as variáveis. Ele apenas controla quanto o algoritmo pode tentar ajustar os coeficientes.

Se aparecer um aviso de que o modelo não convergiu, podemos aumentar max_iter, mas isso não garante que o modelo esteja adequado.

## 10. Hyperparameter tuning

Hyperparameter tuning é procurar valores de hiperparâmetros que produzam bom desempenho em dados não usados para ajustar os parâmetros.

Exemplo:

    alpha = [0.01, 0.1, 1.0, 10.0]
    max_depth = [2, 4, 8, None]
    learning_rate = [0.001, 0.01, 0.1]

Para cada configuração:

1. o hiperparâmetro é definido;
2. o modelo é treinado;
3. os parâmetros são aprendidos no conjunto de treino;
4. o desempenho é medido em validação;
5. a melhor configuração é selecionada.

Exemplo com GridSearchCV:

    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import Ridge

    search = GridSearchCV(
        estimator=Ridge(),
        param_grid={"alpha": [0.01, 0.1, 1.0, 10.0]},
        cv=5,
        scoring="neg_mean_squared_error"
    )

    search.fit(X_train, y_train)

    print(search.best_params_)
    best_model = search.best_estimator_

Os parâmetros finais aprendidos pelo melhor modelo continuam sendo ajustados durante o fit. A busca escolhe o alpha; ela não transforma alpha em coeficiente aprendido.

## 11. Exemplo visual do fluxo

    Dados + hiperparâmetros
              |
              v
        algoritmo de treino
              |
              v
    parâmetros aprendidos
              |
              v
             modelo

Em termos funcionais:

    modelo_final = treinar(X_train, y_train, hyperparameters)

    previsao = modelo_final(X_new)

## 12. Comparação direta

| Item | Quem define? | Quando? | Exemplo |
|---|---|---|---|
| parâmetro | algoritmo | durante fit | coeficiente, peso, intercepto |
| hiperparâmetro | pessoa, busca ou sistema | antes/durante validação | alpha, max_depth, learning_rate |
| métrica | pessoa/equipe | antes da avaliação | accuracy, F1, RMSE |
| previsão | modelo | após treinamento | y_hat |

## 13. Cuidados

O conjunto de teste deve ser usado apenas para a avaliação final. Se escolhermos hiperparâmetros olhando diretamente o teste, o teste deixa de ser imparcial.

O fluxo recomendado é:

    treino -> aprendizado dos parâmetros
    validação/cross-validation -> escolha dos hiperparâmetros
    teste -> avaliação final

Também devemos registrar:

- hiperparâmetros usados;
- versão das bibliotecas;
- dados utilizados;
- métricas;
- parâmetros aprendidos quando necessário;
- seed e configuração do ambiente.

## Resumo

- Parâmetros respondem: “o que o modelo aprendeu dos dados?”
- Hiperparâmetros respondem: “como o modelo deve aprender ou qual complexidade pode ter?”
- learning_rate controla o tamanho dos passos de atualização.
- alpha controla a penalização de pesos grandes.
- max_depth controla a complexidade máxima da árvore.
- hyperparameter tuning procura uma boa configuração usando validação, não o teste final.

## Fonte principal

Documentação do scikit-learn sobre ajuste de hiperparâmetros: https://scikit-learn.org/stable/modules/grid_search.html

