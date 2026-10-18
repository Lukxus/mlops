# Perguntas de revisão

## Compreensão

1. Qual é a diferença entre objetivo de negócio e objetivo do modelo?
2. Por que uma previsão não é automaticamente uma decisão?
3. O que distingue uma feature válida de uma informação futura?
4. Por que o horizonte precisa estar explícito?
5. Quando uma regra é preferível a ML?

## Aplicação

6. Formule “detectar transações suspeitas” com unidade, momento, alvo, horizonte e decisão.
7. Escolha entre classificação, regressão, ranking e anomalia para priorizar alertas de uma equipe limitada.
8. Dê um exemplo de falso positivo e falso negativo em cancelamento de cliente.
9. Proponha um baseline para prever falhas de requisições.
10. Defina uma métrica de negócio que não seja accuracy para um sistema de incidentes.

## Diagnóstico

11. “O cliente não abriu chamado” é um bom rótulo de satisfação? Quais hipóteses seriam necessárias?
12. Uma feature calculada após a confirmação da fraude pode ser usada na autorização? Por quê?
13. Um modelo com AUC maior sempre produz maior valor de negócio? Explique.
14. Se o modelo reduz cancelamentos observados, isso prova que a ação foi causal? Por quê?
15. O que precisa ser monitorado quando os rótulos chegam semanas depois?

## Exercício final

Escreva uma especificação para um sistema que classifica requisições como “provável falha” ou “provável sucesso”. Inclua:

- objetivo de negócio;
- unidade e população;
- momento da previsão;
- features permitidas;
- variável-alvo;
- horizonte;
- decisão;
- custos dos erros;
- baseline;
- métrica de negócio;
- métricas técnicas;
- contrato de produção;
- fallback e monitoramento.

## Próximo passo

Depois de responder às perguntas, avance para `03-dados-e-rotulos`. O primeiro objetivo será transformar a especificação em uma tabela de observações, uma regra de rotulagem e uma estratégia para lidar com atraso, ausência e ruído nos rótulos.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
