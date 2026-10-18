# Visão geral da formulação

## Intuição

Formular um problema de Machine Learning é transformar uma frase ampla, como “reduzir incidentes”, em uma pergunta previsível e verificável:

> Para qual entidade, em qual instante, usando quais informações disponíveis, queremos prever qual evento futuro para apoiar qual decisão?

O modelo é apenas um componente. Antes dele existem uma necessidade de negócio, uma definição observável do evento e uma ação. Depois dele existem avaliação, integração, monitoramento e revisão.

## Problema de negócio versus problema de ML

| Tipo | Exemplo |
|---|---|
| Negócio | Reduzir o impacto de falhas em um serviço crítico. |
| ML | Estimar, antes da execução, a probabilidade de uma requisição falhar nos próximos minutos. |
| Decisão | Fazer retry, mudar a rota ou alertar uma equipe. |

O problema de negócio expressa valor e restrições. O problema de ML expressa uma relação entre entradas disponíveis e um resultado futuro. A decisão define como a previsão será usada.

## Definição formal simplificada

Seja uma unidade de previsão (i), observada no tempo (t), com features (X_{i,t}). O modelo produz:

\[
\hat{p}_{i,t} = f(X_{i,t}) \approx P(Y_{i,t+h}=1 \mid X_{i,t})
\]

em que (Y) é o evento-alvo e (h) é o horizonte. A previsão não é automaticamente a decisão: a aplicação pode aplicar um threshold, uma política, uma regra de segurança ou revisão humana.

## Exemplo pequeno

“Uma transação pode ser fraude” ainda é incompleto. Uma formulação melhor seria:

> No momento da autorização, classificar cada transação como provável fraude ou não fraude, usando somente dados disponíveis até a autorização, para encaminhar casos de alto risco à revisão, considerando confirmação do caso em até 30 dias.

## Fato, inferência e recomendação

- **Fato:** a documentação do Google recomenda definir o resultado desejado, a saída do modelo e as métricas de sucesso separadamente.
- **Inferência:** se a unidade, o tempo e o alvo não estiverem claros, não há como construir corretamente exemplos de treinamento ou avaliar generalização.
- **Recomendação:** escreva a especificação antes de abrir um notebook ou escolher um algoritmo.

## Quando não usar ML

Uma regra determinística é preferível quando a política é conhecida, estável, auditável e cobre suficientemente os casos. ML passa a ser candidato quando há padrões difíceis de enumerar, dados históricos representativos, um alvo observável e uma decisão cujo benefício justifica o custo de coleta, treinamento e operação.

## Consequências para o projeto

Uma formulação ruim contamina todas as etapas seguintes: dados podem ser coletados para o alvo errado, o split pode usar o futuro, a métrica pode não refletir o custo operacional e o serviço pode produzir uma saída que nenhum consumidor sabe interpretar.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
