# Formulação e operação em produção

## Da especificação ao serviço

A formulação define o contrato que será implementado:

1. quais eventos entram;
2. quais features são calculadas;
3. qual saída é retornada;
4. qual decisão consome a saída;
5. que fallback ocorre em erro, timeout ou baixa confiança;
6. que métricas são observadas.

## Sistemas corporativos

Uma arquitetura típica pode envolver:

- API Gateway recebendo a requisição;
- serviço de features ou agregações históricas;
- serviço de inferência;
- motor de decisão;
- fila para revisão humana;
- armazenamento de previsões e resultados posteriores;
- pipeline de treinamento e monitoramento.

O modelo não deve assumir que o consumidor conhece detalhes internos. O contrato precisa declarar tipos, unidades, limites, versão, latência esperada e comportamento de indisponibilidade.

## Observabilidade

Além de CPU, memória e latência, acompanhe:

- taxa de valores ausentes;
- distribuição das features;
- distribuição dos scores;
- proporção de decisões por classe;
- taxa de fallback;
- atraso dos rótulos;
- desempenho quando o rótulo finalmente chega;
- mudanças na população prevista.

## Feedback loops

Uma decisão altera o comportamento observado. Bloquear uma transação impede que o resultado real seja observado; alertar uma equipe aumenta a chance de um caso ser investigado; oferecer retenção muda a probabilidade de cancelamento. Portanto, os dados futuros podem depender do próprio modelo.

## Fato, inferência e recomendação

- **Fato:** Sculley et al. descrevem dependências de dados, feedback loops, consumidores não declarados e mudanças no mundo como riscos de sistemas de ML.
- **Inferência:** uma formulação que ignora operação pode ser estatisticamente válida offline e ainda falhar como produto.
- **Recomendação:** registre decisões, versões e resultados posteriores com correlação distribuída suficiente para reconstruir o caminho de uma previsão.

## Critério de produção

“Modelo aprovado” deve significar mais do que métrica no conjunto de teste. Deve incluir validade da entrada, disponibilidade da saída, custo da decisão, fallback, monitoramento, segurança, governança e plano de atualização.

## Fonte principal

[Sculley et al. — Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
