# Dúvidas e respostas sobre formulação do problema

Este arquivo registra dúvidas surgidas durante o estudo e as respostas correspondentes.

## 1. Como interpretar a fórmula da previsão?

A fórmula correta é:

\[
\hat{p}_{i,t} = f(X_{i,t}) \approx P(Y_{i,t+h}=1 \mid X_{i,t})
\]

A ideia em linguagem comum é:

> Usando as informações disponíveis agora, o modelo estima a chance de um evento acontecer no futuro.

### Exemplo

Considere uma transação com:

- valor de R$ 900;
- país do cliente;
- horário da compra;
- histórico de transações recentes.

Essas informações formam as features (X_{i,t}). O modelo (f) recebe essas informações e retorna, por exemplo:

\[
\hat{p}_{i,t}=0{,}82
\]

Isso significa que o modelo estima uma probabilidade de 82% de a transação ser confirmada como fraude dentro do horizonte definido.

### Significado dos símbolos

| Símbolo | Significado |
|---|---|
| (i) | Unidade observada, como uma transação, cliente ou requisição. |
| (t) | Momento em que a previsão é feita. |
| (X_{i,t}) | Informações disponíveis para a unidade (i) no momento (t). |
| (f) | Modelo treinado. |
| (hat{p}_{i,t}) | Probabilidade estimada pelo modelo. |
| (Y) | Evento real que queremos prever. |
| (h) | Horizonte futuro da previsão. |
| (Y=1) | O evento aconteceu. |
| (mid) | “Dado que” ou “considerando que”. |

A parte condicional:

\[
P(Y_{i,t+h}=1 \mid X_{i,t})
\]

significa:

> A probabilidade de o evento acontecer no futuro, considerando as informações que conhecemos agora.

O símbolo (approx) aparece porque a probabilidade verdadeira não é conhecida diretamente. O modelo aprende uma aproximação usando exemplos históricos.

### Previsão não é decisão

O modelo pode produzir:

```text
probabilidade = 0,82
```

Depois, uma política pode aplicar um threshold:

```text
se probabilidade >= 0,70:
    enviar para revisão
senão:
    aprovar automaticamente
```

Portanto:

```text
informações atuais -> modelo -> probabilidade -> regra -> decisão
```

A probabilidade é a previsão. “Enviar para revisão” é a decisão.

## 2. Em que momento entram guardrails e regras de limite?

Guardrails são restrições que impedem que a previsão ou a decisão ultrapasse limites aceitáveis.

Eles podem entrar:

1. antes do modelo, filtrando entradas inválidas;
2. durante o treinamento, por meio de restrições ou objetivos específicos;
3. depois da previsão, limitando ou ajustando o resultado;
4. na camada de decisão em produção, aplicando regras, fallback e revisão humana.

Em muitos sistemas corporativos, regras como “a meta não pode ser negativa” ficam depois da previsão, na camada de política ou decisão.

### Exemplo: previsão de metas comerciais

Suponha que o modelo estime o potencial de vendas:

| Funcionário | Região | Previsão do modelo |
|---|---|---:|
| Ana | Alta procura | 120 |
| Bruno | Pouca procura | -4 |
| Carla | Pouca procura | 0,5 |

Se a regra de negócio disser que a meta mínima é 10:

\[
\text{meta final}=\max(\text{previsão do modelo},\text{meta mínima})
\]

| Funcionário | Previsão | Meta mínima | Meta final |
|---|---:|---:|---:|
| Ana | 120 | 10 | 120 |
| Bruno | -4 | 10 | 10 |
| Carla | 0,5 | 10 | 10 |

O fluxo fica:

```text
dados históricos
      -> modelo prevê potencial
      -> guardrails e regras de negócio
      -> meta final aprovada
      -> sistema comercial
```

O modelo estima o potencial. A política define limites. A decisão aplica a regra.

### Tipos comuns de guardrail

Limite inferior:

\[
y_{final}=\max(\hat{y},y_{min})
\]

Limite superior:

\[
y_{final}=\min(\hat{y},y_{max})
\]

Intervalo permitido:

\[
y_{final}=\min(\max(\hat{y},y_{min}),y_{max})
\]

Também podem existir:

- fallback para uma meta histórica quando o modelo falha;
- revisão humana quando a previsão muda muito em relação ao período anterior;
- limite de variação, como no máximo 20% de aumento mensal;
- restrições de capacidade da região;
- regras de elegibilidade ou exclusão.

### Guardrail não é objetivo de negócio

O objetivo pode ser:

> prever o potencial de vendas.

O guardrail pode ser:

> garantir que a meta não seja menor que o mínimo operacional.

São camadas diferentes. Além disso, prever vendas e definir metas não são necessariamente o mesmo problema de ML:

1. previsão de vendas: regressão;
2. definição de metas com limites: previsão mais regras;
3. distribuição de uma meta total: otimização com restrições;
4. decisão sobre atingir ou não a meta: classificação.

Os limites precisam ser validados com o negócio. Uma meta mínima pode ter efeitos sobre justiça, motivação, comparação entre regiões e avaliação dos funcionários.

## 3. O que é churn?

Churn significa cancelamento, abandono ou perda de um cliente.

Em uma empresa de assinatura, um cliente pode sofrer churn quando:

- cancela o plano;
- não renova;
- encerra a conta;
- deixa de utilizar o serviço durante um período definido.

Uma formulação possível é:

> Para cada cliente ativo hoje, prever se ele cancelará o serviço nos próximos 30 dias, usando somente informações disponíveis até hoje, para priorizar ações de retenção.

| Elemento | Exemplo |
|---|---|
| Unidade | Cliente ativo. |
| Momento | Hoje. |
| Features | Uso, pagamentos, chamados, plano e histórico anterior. |
| Variável-alvo | Cliente cancelou. |
| Horizonte | Próximos 30 dias. |
| Decisão | Priorizar contato de retenção. |

A variável-alvo pode ser definida como:

\[
Y=\begin{cases}
1, & \text{se o cliente cancelar nos próximos 30 dias}\\
0, & \text{caso contrário}
\end{cases}
\]

Se o modelo produzir:

\[
\hat{p}=0{,}75
\]

isso significa:

> O modelo estima 75% de chance de o cliente cancelar dentro dos próximos 30 dias.

A empresa poderia definir:

```text
se probabilidade >= 0,60:
    priorizar para retenção
senão:
    seguir tratamento normal
```

### O que não é necessariamente churn?

Um cliente que não acessou o sistema por três dias não necessariamente cancelou. Ele pode estar viajando, usando outro canal ou simplesmente ter uma frequência de uso menor.

Por isso, churn precisa de uma definição operacional. Exemplos diferentes são:

- cancelamento explícito;
- não renovação;
- 60 dias sem uso;
- encerramento financeiro;
- ausência de atividade após uma tentativa de cobrança.

Cada definição cria um problema de ML diferente, com dados, rótulos e horizonte diferentes.

## Fonte principal

[Google for Developers — Framing an ML problem](https://developers.google.com/machine-learning/problem-framing/ml-framing)
