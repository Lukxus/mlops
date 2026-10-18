# Convergência, max_iter e Grid Search

## 1. O que significa convergir?

Treinar muitos modelos significa procurar parâmetros que reduzam uma função de perda.

Por exemplo, em regressão logística, o algoritmo procura coeficientes que produzam boas probabilidades para as classes.

A cada passo, ele atualiza os parâmetros:

    theta_novo = theta_atual - passo * gradiente

O algoritmo converge quando novas atualizações deixam de produzir mudanças relevantes na função de perda ou nos parâmetros.

Em termos intuitivos:

- antes da convergência: o modelo ainda está encontrando uma solução melhor;
- próximo da convergência: as melhorias ficam pequenas;
- convergiu: a solução está suficientemente estável para o critério definido.

Convergência não significa que o modelo encontrou a verdade ou que obteve a melhor métrica possível. Significa que o processo de otimização terminou de forma estável segundo um critério numérico.

## 2. O que é max_iter?

Em:

    LogisticRegression(max_iter=2000)

max_iter é o número máximo de passos que o algoritmo de otimização pode executar em um único treinamento.

Ele não significa:

- 2000 modelos diferentes;
- 2000 valores de hiperparâmetros;
- 2000 tentativas do Grid Search;
- 2000 exemplos do dataset.

Ele significa, aproximadamente:

    parâmetros iniciais
        -> atualização 1
        -> atualização 2
        -> ...
        -> atualização 2000

O algoritmo pode parar antes se convergir.

## 3. Se eu aumentar de 1000 para 2000, o modelo melhora?

Depende.

### Caso 1: já convergia antes de 1000

Aumentar para 2000 não deve mudar o resultado de forma relevante. O algoritmo já havia terminado porque encontrou uma solução estável.

### Caso 2: não convergia em 1000

Aumentar para 2000 pode permitir que o otimizador continue e encontre uma solução estável.

Porém, isso não garante melhora na generalização. Pode apenas eliminar um aviso de convergência.

### Caso 3: o problema está mal preparado

Aumentar indefinidamente max_iter pode esconder problemas como:

- features em escalas muito diferentes;
- dados com separação quase perfeita;
- regularização inadequada;
- outliers;
- solver incompatível;
- colunas redundantes;
- modelo excessivamente complexo.

Em muitos casos, scaling ajuda o otimizador a convergir mais rapidamente.

## 4. Exemplo numérico

Suponha que a função de perda apresente estes valores:

| iteração | perda |
|---:|---:|
| 1 | 10,0 |
| 10 | 4,2 |
| 100 | 1,8 |
| 500 | 1,21 |
| 800 | 1,2001 |
| 900 | 1,2000 |

Se a tolerância aceitar variações menores que 0,0001, o algoritmo pode considerar que convergiu próximo da iteração 900.

Se max_iter=500, ele para antes de convergir. Se max_iter=2000, ele consegue chegar à região estável.

## 5. max_iter é hiperparâmetro?

Sim. max_iter é um hiperparâmetro do processo de otimização.

Mas ele não é um parâmetro aprendido pelo modelo.

Exemplo:

    LogisticRegression(max_iter=2000)

- max_iter: configuração do algoritmo;
- coef_: coeficientes aprendidos;
- intercept_: intercepto aprendido.

## 6. Isso é Grid Search?

Não diretamente.

max_iter controla os passos internos de um único ajuste:

    modelo.fit(X_train, y_train)

Grid Search controla várias configurações de hiperparâmetros. Por exemplo:

    param_grid = {
        "C": [0.1, 1.0, 10.0],
        "max_iter": [500, 1000, 2000]
    }

O Grid Search pode treinar várias combinações:

| C | max_iter |
|---:|---:|
| 0,1 | 500 |
| 0,1 | 1000 |
| 0,1 | 2000 |
| 1,0 | 500 |
| 1,0 | 1000 |
| 1,0 | 2000 |
| 10,0 | 500 |
| 10,0 | 1000 |
| 10,0 | 2000 |

Com 3 valores de C e 3 valores de max_iter, são 9 configurações. Se houver validação cruzada com 5 folds, podem ocorrer até:

    9 * 5 = 45 treinamentos

Em cada treinamento individual, max_iter continua sendo o limite de passos internos.

## 7. A diferença em uma frase

- max_iter: quantos passos um treinamento pode dar para ajustar uma configuração;
- Grid Search: quantas configurações diferentes serão comparadas;
- convergência: condição para saber se um treinamento estabilizou.

## 8. Exemplo com GridSearchCV

    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import LogisticRegression

    search = GridSearchCV(
        estimator=LogisticRegression(random_state=42),
        param_grid={
            "C": [0.1, 1.0, 10.0],
            "max_iter": [500, 1000, 2000]
        },
        cv=5,
        scoring="f1"
    )

    search.fit(X_train, y_train)

    print(search.best_params_)

O Grid Search pode escolher uma configuração com max_iter=2000 porque ela convergiu melhor, mas isso não significa que 2000 seja sempre melhor que 1000.

## 9. Como diagnosticar um aviso de convergência?

Uma sequência prática é:

1. verificar se as features foram escaladas;
2. conferir valores extremos e nulos;
3. testar outro solver compatível;
4. aumentar max_iter moderadamente;
5. verificar a regularização;
6. comparar validação e teste;
7. investigar se o modelo está adequado ao problema.

Aumentar max_iter é uma tentativa de dar mais tempo ao otimizador. Não é substituto para diagnóstico.

## Resumo

- Convergir é estabilizar a busca por parâmetros.
- max_iter é o limite de passos internos de um treinamento.
- 1000 não é automaticamente pior que 2000.
- Se o modelo já convergiu em 1000, aumentar para 2000 normalmente não muda nada.
- Se não convergiu, aumentar pode ajudar.
- Grid Search é uma camada externa que compara valores de hiperparâmetros.
- Cada combinação do Grid Search executa seu próprio treinamento e possui seu próprio max_iter.

## Fonte principal

Documentação do scikit-learn sobre LogisticRegression e max_iter: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

