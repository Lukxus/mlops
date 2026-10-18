# Negócio, modelo e decisão

## Três camadas diferentes

### Objetivo de negócio

É o resultado que a organização deseja obter: reduzir perdas, diminuir indisponibilidade, atender clientes mais rapidamente ou diminuir cancelamentos.

### Objetivo do modelo

É a tarefa estatística que o modelo executará: estimar uma probabilidade, prever um valor, ordenar itens ou identificar padrões atípicos.

### Decisão

É a ação tomada após a previsão: aprovar, bloquear, priorizar, escalar, fazer retry ou não agir.

Uma única previsão pode alimentar decisões diferentes. Por isso, “o modelo tem boa acurácia” não prova que o sistema produz valor.

## Previsão não é causalidade

- **Associação:** duas variáveis aparecem relacionadas nos dados.
- **Previsão:** as entradas ajudam a antecipar um resultado futuro.
- **Causalidade:** mudar uma variável produziria uma mudança no resultado sob hipóteses e intervenção definidas.

Um modelo que prevê cancelamento pode usar quantidade de chamados. Isso não significa que reduzir chamados causará menor cancelamento. A feature pode apenas sinalizar insatisfação já existente.

## Exemplo corporativo

Objetivo de negócio: reduzir o tempo de recuperação de incidentes.

Objetivo do modelo: estimar se um evento de observabilidade será confirmado como incidente severo nos próximos 15 minutos.

Decisão: enviar para a equipe de plantão, agrupar com outro alerta ou ignorar.

Métrica do modelo: recall para incidentes severos sob um limite de falsos positivos.

Métrica de negócio: redução do tempo médio até reconhecimento e do tempo até recuperação, sem aumento inaceitável de fadiga de alertas.

## Critério de qualidade

Uma formulação deve responder, separadamente:

1. Qual resultado humano ou organizacional desejamos?
2. Qual resultado o modelo consegue estimar?
3. Qual decisão será tomada?
4. Como saberemos se a decisão melhorou o sistema?

## Fato, inferência e recomendação

- **Fato:** métricas de sucesso do produto são diferentes de métricas como accuracy, precision, recall e AUC.
- **Inferência:** otimizar apenas a métrica técnica pode incentivar decisões que aumentam o custo operacional.
- **Recomendação:** documente explicitamente o responsável pela decisão, o fallback e o que ocorre quando o modelo está indisponível.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
