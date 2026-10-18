# Métricas, custos e baseline

## Métrica de negócio versus métrica do modelo

- **Métrica de negócio:** mede o efeito no processo, como perda líquida, tempo de recuperação, conversão ou volume de chamados.
- **Métrica do modelo:** mede a qualidade preditiva, como precision, recall, F1, log loss ou AUC.

Uma métrica de modelo é um meio de avaliação; não é automaticamente o objetivo final.

## Falsos positivos e falsos negativos

Em fraude:

- falso positivo: transação legítima marcada como suspeita;
- falso negativo: fraude liberada como normal.

O custo de cada erro pode ser diferente. Uma política pode aceitar mais revisões manuais para reduzir perdas, ou aceitar algum risco para preservar conversão.

Uma forma simples de expressar o custo esperado é:

\[
E[C] = C_{FP}P(FP) + C_{FN}P(FN) + C_{operacional}
\]

Na prática, esses custos são estimativas e devem ser validados com o negócio.

## Threshold

Um classificador pode produzir um score ou probabilidade. A aplicação transforma esse valor em ação usando um limiar. Alterar o threshold modifica o trade-off entre falsos positivos e falsos negativos, mesmo sem retreinar o modelo.

## Critérios de sucesso antes do treinamento

Exemplo:

- reduzir perda financeira em pelo menos 10%;
- manter recusas indevidas abaixo de 0,5%;
- manter p95 da decisão abaixo de 80 ms;
- permitir fallback para regra existente;
- monitorar desempenho quando os rótulos atrasados chegarem.

## Baseline

Compare o modelo com:

1. processo manual atual;
2. regra de negócio existente;
3. sempre escolher a classe majoritária;
4. uma estatística simples ou score histórico.

Se o modelo não superar o baseline sob as restrições reais, ainda não há evidência de valor.

## Fato, inferência e recomendação

- **Fato:** documentação do scikit-learn descreve a decisão binária como aplicação de um threshold sobre um score.
- **Inferência:** separar score de decisão facilita alterar a política sem mudar necessariamente o modelo.
- **Recomendação:** registre threshold, versão do modelo, versão das features e política aplicada em cada decisão.

## Fonte principal

[scikit-learn — Tuning the decision threshold for class prediction](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)
