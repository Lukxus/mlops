# Exemplos bem e mal formulados

## Exemplo 1 — fraude

### Bem formulado

> Para cada transação submetida à autorização, estimar a probabilidade de fraude confirmada nos 30 dias seguintes, usando somente dados disponíveis até a autorização, para decidir entre aprovar, revisar ou bloquear.

Há unidade, tempo, features, alvo, horizonte e decisão.

### Mal formulado

> Criar um modelo para detectar fraudes.

Não define o que é uma fraude confirmada, quando a previsão ocorre, que transações entram na população, qual ação será tomada nem qual custo é aceitável.

## Exemplo 2 — falha de requisição

### Bem formulado

> Antes de chamar o provedor de pagamentos, prever se a requisição terá timeout ou resposta 5xx nos próximos 30 segundos, usando telemetria e histórico disponíveis até aquele instante, para escolher retry limitado ou rota alternativa.

### Mal formulado

> Prever quais APIs são ruins.

“Ruim” pode significar latência, erro, custo, indisponibilidade ou experiência do usuário. A formulação mistura serviço, requisição e janela temporal.

## Exemplo 3 — churn

### Bem formulado

> A cada renovação semanal, estimar se um cliente ativo cancelará nos próximos 30 dias, usando atividade registrada antes da renovação, para priorizar contato de retenção.

### Mal formulado

> Prever churn com todas as colunas do cadastro.

O cadastro pode conter campos preenchidos depois do cancelamento ou variáveis que codificam diretamente o resultado.

## Exemplo 4 — incidentes

### Bem formulado

> Para cada alerta recebido pelo serviço de observabilidade, estimar se ele será confirmado como incidente severo em até 15 minutos, para priorizar a fila da equipe de plantão.

### Mal formulado

> Classificar logs em bons e ruins.

Logs não são necessariamente a unidade de decisão e “bom” ou “ruim” não são rótulos operacionais.

## Lição comum

Uma formulação boa contém uma ação possível. Se nenhuma decisão muda após a previsão, o modelo pode ser apenas uma análise descritiva, não um componente operacional.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
