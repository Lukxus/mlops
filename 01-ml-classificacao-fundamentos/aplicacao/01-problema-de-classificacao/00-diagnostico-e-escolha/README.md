# Diagnóstico e escolha do modelo

Este diretório reúne o protocolo usado depois de cada experimento.

## Perguntas de diagnóstico

- O alvo é numérico e contínuo?
- Há uma relação aproximadamente linear?
- O tempo altera a forma correta de dividir os dados?
- Existem outliers relevantes ou apenas erros de medição?
- A variância dos erros muda ao longo da faixa de previsão?
- As variáveis explicativas são muito correlacionadas?
- Há mais features do que observações úteis?
- O modelo precisa extrapolar ou apenas interpolar?
- Há interações e limiares que uma reta não representa?
- O resultado melhora sobre um baseline simples em dados não vistos?

## Artefatos esperados

- gráfico dos dados e das previsões;
- gráfico dos resíduos;
- tabela de métricas;
- registro das hipóteses;
- decisão: manter, substituir ou investigar o modelo.
