# Especificação formal do problema

## A unidade de previsão

É a entidade para a qual uma previsão será produzida: uma transação, requisição, cliente, sessão, alerta ou janela de tempo.

Se a unidade não estiver definida, amostras podem ser duplicadas, misturadas ou avaliadas com granularidades diferentes.

## População prevista

Defina quem ou o que entra no escopo. Exemplos:

- todas as transações online acima de determinado valor;
- requisições ao serviço de pagamentos;
- clientes ativos há pelo menos 30 dias;
- eventos produzidos por serviços críticos.

A população de treino precisa representar a população que receberá previsões, respeitando as mudanças de tempo e contexto.

## Momento da previsão

É o instante em que o sistema precisa produzir o resultado. Ele cria um corte temporal: features posteriores não podem ser utilizadas como se fossem conhecidas.

## Features disponíveis

Uma feature válida está disponível com qualidade aceitável no momento da previsão. “Disponível no banco” não significa necessariamente “disponível no instante operacional”: ela pode chegar atrasada, ser calculada depois ou depender do resultado.

## Variável-alvo e horizonte

O alvo é o evento observável que será associado à unidade. O horizonte define até quando o evento será considerado.

Exemplo:

\[
Y_{i,t}^{(24h)} = 1
\]

se o cliente (i), observado em (t), cancelar entre (t) e (t+24) horas.

## Tabela de formulação

| Elemento | Pergunta que deve ser respondida | Exemplo |
|---|---|---|
| Objetivo de negócio | Que resultado queremos melhorar? | Reduzir perdas por fraude sem bloquear clientes legítimos. |
| Unidade de previsão | Para qual entidade prevemos? | Uma transação. |
| Momento da previsão | Quando o resultado precisa estar disponível? | Antes da autorização. |
| Feature | Que informação já existe nesse instante? | Valor, horário, canal e histórico anterior. |
| Variável-alvo | Que evento será observado? | Fraude confirmada. |
| Horizonte | Por quanto tempo observamos o futuro? | Até 30 dias após a transação. |
| Decisão | Que ação a previsão influencia? | Aprovar, revisar ou bloquear. |
| Métrica de sucesso | Qual resultado indica melhoria? | Menor perda líquida sem aumento excessivo de recusas. |

## Forma matemática

Uma formulação supervisionada pode ser descrita como:

\[
(X_{i,t}, Y_{i,t+h}, a, C, M)
\]

em que (X) são features disponíveis em (t), (Y) é o evento observado no horizonte (h), (a) é a ação, (C) representa custos e restrições, e (M) representa métricas.

## Exemplo aplicado a requisições

- Unidade: requisição HTTP.
- População: requisições ao endpoint de pagamento.
- Momento: imediatamente antes da chamada ao provedor externo.
- Features: serviço, rota, método, região, horário e histórico anterior agregado.
- Alvo: resposta 5xx ou timeout durante os próximos 30 segundos.
- Decisão: retry limitado ou rota alternativa.

## Consequências

Essa especificação determina a consulta de dados, a construção do rótulo, o split temporal, o contrato da API e o monitoramento de atraso do rótulo.

## Fonte principal

[Google for Developers — Implementing a model](https://developers.google.com/machine-learning/problem-framing/implement-model)
