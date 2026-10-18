# Scikit-learn versus PyTorch

## Scikit-learn

É uma biblioteca de alto nível para Machine Learning supervisionado e não supervisionado. Oferece estimators prontos, pré-processamento, pipelines, métricas, validação cruzada e busca de hiperparâmetros.

```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

É a escolha inicial para regressão, classificação, árvores, ensembles e dados tabulares.

## PyTorch

É uma biblioteca baseada em tensores e grafos computacionais, com cálculo automático de gradientes. Permite controlar explicitamente modelo, função de perda, gradientes, otimizador e loop de treinamento.

```python
loss.backward()
optimizer.step()
```

É mais adequado para redes neurais, deep learning, imagens, texto, áudio e modelos customizados.

## Regra prática

Use Scikit-learn para consolidar ML clássico e avaliação. Use PyTorch quando for necessário construir ou treinar modelos neurais com maior controle.

Fontes: https://scikit-learn.org/stable/getting_started.html e https://docs.pytorch.org/tutorials/beginner/basics/intro.html
