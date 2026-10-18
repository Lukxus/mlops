# Escolha da tarefa e saída esperada

## Escolha orientada pela decisão

| Tarefa | Saída típica | Quando considerar |
|---|---|---|
| Classificação | Classe ou probabilidade | Existem categorias ou uma decisão discreta. |
| Regressão | Valor numérico | A quantidade prevista importa diretamente. |
| Ranking | Ordem ou score relativo | É necessário priorizar itens. |
| Detecção de anomalias | Score de atipicidade | Há poucos ou nenhum rótulo confiável de eventos raros. |
| Regras | Decisão determinística | A política é conhecida e estável. |
| Nenhum ML | Consulta, agregação ou processo manual | O custo e o risco do ML não se justificam. |

## Classificação versus regressão

Se o sistema precisa responder “acionar ou não acionar” com categorias estáveis, classificação pode ser apropriada. Se a ação depende de limites que mudam continuamente, prever um valor ou probabilidade e aplicar o limite na aplicação pode ser mais flexível.

## Saída do modelo

Defina o contrato antes do treinamento:

```json
{
  "prediction": "suspeito",
  "probability": 0.87,
  "model_version": "fraud-2026-01",
  "decision_reason": "score_acima_do_threshold"
}
```

O campo `prediction` pode ser uma classe; `probability` pode apoiar thresholds e priorização; `model_version` é necessário para auditoria; a razão deve ser usada somente se puder ser produzida de modo correto e compreensível.

## Quando ML não é necessário

Não é necessário quando:

- a regra é completa e estável;
- o evento é raro demais para obter sinais e rótulos úteis;
- não há ação que mude após a previsão;
- o custo de erro ou de explicação é incompatível;
- uma consulta ou agregação resolve diretamente;
- a operação não consegue monitorar e manter o sistema.

## Exemplos

- **Normal ou suspeito:** classificação binária, se há confirmação histórica de suspeita.
- **Qual cliente priorizar:** ranking, se o objetivo é ordenar casos para uma equipe limitada.
- **Tempo até recuperação:** regressão ou previsão de distribuição, se o valor numérico orienta planejamento.
- **Evento desconhecido em logs:** detecção de anomalias, se não há rótulos suficientes.

## Recomendação prática

Escolha a saída que representa a decisão real com o menor grau de transformação intermediária. Se a aplicação precisa ordenar 10 mil casos, uma classe binária pode desperdiçar informação; se precisa apenas bloquear ou liberar, uma saída complexa pode ser desnecessária.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
