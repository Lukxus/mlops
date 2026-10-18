# Ecossistema de bibliotecas de Machine Learning

## Scikit-learn

Biblioteca de alto nível para Machine Learning clássico. Oferece estimators para regressão, classificação, clustering e redução de dimensionalidade, além de pré-processamento, pipelines, métricas, validação cruzada e busca de hiperparâmetros.

É a primeira escolha do projeto para dados tabulares e modelos clássicos.

## PyTorch

Framework de tensores e cálculo automático de gradientes. Dá maior controle sobre modelos, funções de perda, otimização, treinamento em GPU e arquiteturas neurais.

É adequado para deep learning, imagens, texto, áudio e modelos customizados.

## TensorFlow e Keras

TensorFlow é uma plataforma de Machine Learning com recursos para construir, treinar e disponibilizar modelos em servidores, dispositivos móveis, edge e JavaScript.

Keras é a API de alto nível recomendada para construir modelos com TensorFlow, oferecendo camadas, modelos, treinamento e utilitários com menor complexidade inicial.

## Outras bibliotecas relevantes

| Biblioteca | Papel principal |
|---|---|
| XGBoost | Gradient boosting eficiente para dados tabulares |
| LightGBM | Gradient boosting eficiente em grandes conjuntos tabulares |
| CatBoost | Gradient boosting com bom suporte a variáveis categóricas |
| JAX | NumPy com autodiferenciação, compilação e aceleração |
| statsmodels | Estatística inferencial e modelos estatísticos interpretáveis |
| Hugging Face Transformers | Modelos pré-treinados e fine-tuning para texto, visão e multimodalidade |
| MLflow | Rastreamento de experimentos, modelos e ciclo de vida |

## Regra prática

```text
Dados tabulares e ML clássico       -> Scikit-learn
Redes neurais e treinamento custom -> PyTorch ou TensorFlow/Keras
Árvores com boosting               -> XGBoost, LightGBM ou CatBoost
Inferência estatística             -> statsmodels
Modelos pré-treinados              -> Hugging Face
Rastreamento e operação            -> MLflow e ferramentas de MLOps
```

Essas bibliotecas se complementam. A escolha deve partir do tipo de problema, dos dados, da necessidade de controle, do hardware e do modo de disponibilização do modelo.

Fontes:

- https://scikit-learn.org/stable/getting_started.html
- https://www.tensorflow.org/about
- https://www.tensorflow.org/guide/keras
- https://docs.pytorch.org/tutorials/beginner/basics/intro.html
- https://xgboost.readthedocs.io/
