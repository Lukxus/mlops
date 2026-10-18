# ML aplicado — fundamentos de classificação

Este é o primeiro bloco da trilha de transição para ML Engineering/MLOps.

## Objetivo

Aprender a treinar, avaliar e explicar um modelo de classificação simples, entendendo os principais riscos antes de colocá-lo em produção.

## Escopo

- Separação entre treino, validação e teste
- Data leakage
- Preprocessing: valores ausentes, encoding e scaling
- Baseline com regressão logística
- Métricas: precision, recall, F1, ROC-AUC e PR-AUC
- Comparação com Random Forest ou XGBoost
- Relação entre métricas e custo de falso positivo/falso negativo

## Organização

- `teoria/`: conceitos, definições, exemplos e perguntas de revisão
- `aplicacao/`: notebooks e código executável
- `dados/`: datasets locais ou instruções para obtê-los
- `notas/`: dúvidas, conclusões e decisões tomadas

## Entrega do bloco

Um notebook ou script que:

1. carregue um dataset de classificação;
2. separe corretamente treino, validação e teste;
3. aplique preprocessing sem vazamento;
4. treine uma regressão logística como baseline;
5. calcule e interprete as principais métricas;
6. compare o baseline com um segundo modelo;
7. documente limitações e próximos passos.

## Sequência de estudo

1. Estudar a teoria em `teoria/`.
2. Registrar dúvidas e aprendizados em `notas/`.
3. Implementar a primeira versão em `aplicacao/`.
4. Revisar os resultados e documentar o que pode falhar em produção.
