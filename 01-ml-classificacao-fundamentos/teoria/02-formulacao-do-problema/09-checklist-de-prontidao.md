# Checklist de prontidão para dados e rótulos

Considere o problema pronto para avançar para `03-dados-e-rotulos` somente quando as respostas forem registradas.

## Negócio e decisão

- [ ] O objetivo de negócio está escrito em termos de resultado.
- [ ] Existe uma decisão ou ação associada à previsão.
- [ ] O responsável pela decisão está identificado.
- [ ] O fallback está definido.

## População e tempo

- [ ] A unidade de previsão está definida.
- [ ] A população está delimitada.
- [ ] O momento da previsão está definido.
- [ ] O horizonte está definido.
- [ ] A janela de observação não usa informação futura.

## Dados e rótulos

- [ ] Cada feature está disponível no momento correto.
- [ ] A variável-alvo é observável ou possui uma regra de mensuração documentada.
- [ ] O atraso do rótulo é conhecido.
- [ ] Proxies e limitações foram registrados.
- [ ] Há exemplos suficientes e representativos para avaliar o caso.

## Avaliação

- [ ] Os custos de falsos positivos e falsos negativos foram discutidos.
- [ ] A métrica de negócio foi definida.
- [ ] As métricas técnicas foram escolhidas antes do treinamento.
- [ ] Existe um baseline manual, heurístico ou ingênuo.
- [ ] O threshold ou a política de decisão está especificado.

## Operação

- [ ] O contrato de entrada e saída está definido.
- [ ] Os limites de latência e disponibilidade são conhecidos.
- [ ] Existe estratégia de logging e observabilidade.
- [ ] Está definido como detectar degradação e mudança de distribuição.
- [ ] Há plano de revisão, retreinamento ou desativação.

## Decisão final

- **Pronto:** todos os itens essenciais estão respondidos e os riscos são aceitáveis.
- **Incompleto:** há perguntas que precisam ser respondidas com stakeholders.
- **Não usar ML agora:** não há alvo, ação, dados representativos ou benefício suficiente.

## Fonte principal

[NIST — AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)
