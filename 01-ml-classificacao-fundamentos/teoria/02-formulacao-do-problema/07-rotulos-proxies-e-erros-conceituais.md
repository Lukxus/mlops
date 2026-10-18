# Rótulos, proxies e erros conceituais

## Conceito desejado versus rótulo observado

O negócio pode desejar “cliente satisfeito”, “transação fraudulenta” ou “incidente relevante”. O dataset precisa de uma regra observável para marcar exemplos. Essa regra é o rótulo.

O rótulo pode ser atrasado, incompleto, inconsistente ou produzido por decisões humanas já influenciadas por políticas anteriores.

## Proxy label

Quando o conceito ideal não é diretamente observável, usa-se uma aproximação. Por exemplo, “vídeo útil” pode ser aproximado por assistir até o fim, compartilhar ou retornar ao vídeo. Cada proxy possui vieses próprios e pode incentivar comportamento indesejado.

O proxy deve ser tratado como hipótese de mensuração, não como verdade absoluta.

## Exemplos corporativos

- “Não houve chamado” não significa necessariamente “cliente satisfeito”.
- “Não foi aberto incidente” não significa “serviço estava normal”.
- “Transação não contestada” não significa necessariamente “não era fraude”.
- “Retry funcionou” não prova que o modelo causou menor indisponibilidade.

## Erros conceituais comuns

1. Usar informação posterior ao momento da previsão.
2. Confundir ausência de evidência com evidência de ausência.
3. Definir o alvo pela coluna mais fácil, e não pelo resultado desejado.
4. Misturar unidades, como treinar por cliente e servir por requisição.
5. Alterar a política operacional e continuar comparando rótulos como se fossem estáveis.
6. Confundir correlação preditiva com variável causal.
7. Ignorar exemplos sem confirmação ou com rótulo atrasado.

## Como reduzir o risco

- definir a regra de rotulagem por escrito;
- registrar o instante em que o rótulo se torna conhecido;
- amostrar casos para revisão humana;
- medir discordância entre anotadores quando houver julgamento;
- documentar limitações do proxy;
- avaliar o modelo também por subpopulações e cenários operacionais.

## Fato, inferência e recomendação

- **Fato:** surveys sobre aprendizado com rótulos ruidosos tratam a incorreção dos rótulos como uma limitação real da aprendizagem supervisionada.
- **Inferência:** se o rótulo representa mal o objetivo, aumentar a complexidade do modelo não corrige o problema de mensuração.
- **Recomendação:** antes de coletar grandes volumes, valide manualmente uma amostra da regra de rotulagem.

## Fonte principal

[Song et al. — Learning from Noisy Labels with Deep Neural Networks: A Survey](https://arxiv.org/abs/2007.08199)
