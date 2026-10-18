# Aplicação

## Objetivo desta etapa

Construir entendimento progressivo sobre regressão: não apenas fazer um modelo funcionar, mas saber escolher a abordagem, justificar a escolha e perceber quando a solução está incorreta.

O primeiro laboratório prático fica em:

`01-problema-de-classificacao/`

Embora a pasta pertença ao primeiro bloco da trilha, começaremos por regressão como base para compreender erro, função de perda, generalização e a ponte para classificação.

## Ordem dos estudos práticos

0. Revisão de fundamentos e ferramentas
1. Regressão linear simples
2. Regressão múltipla
3. Regressão polinomial
4. Regressão regularizada
5. Árvores de regressão
6. Séries temporais

Cada família terá:

- uma versão básica, com poucos dados e uma pergunta controlada;
- uma versão complexa, com ruído, outliers, variáveis adicionais, mudança de distribuição ou risco de leakage;
- uma comparação explícita com alternativas;
- uma decisão documentada sobre quando usar ou não o modelo.

## Ciclo obrigatório de cada projeto

1. Definir o problema e a variável-alvo.
2. Formular uma hipótese sobre a relação entre entrada e saída.
3. Criar um baseline simples.
4. Escolher a divisão dos dados.
5. Treinar o modelo.
6. Avaliar com mais de uma métrica.
7. Inspecionar previsões e resíduos.
8. Procurar sinais de solução incorreta.
9. Comparar com outro modelo.
10. Registrar a decisão e os trade-offs.

## Como identificar uma solução possivelmente incorreta

Antes de estudar tipos específicos de erro, vamos procurar sinais gerais:

- desempenho excelente no treino e ruim em dados não vistos;
- métricas incompatíveis com a realidade do problema;
- resíduos com padrão visível em vez de comportamento aproximadamente aleatório;
- erros que aumentam conforme o valor previsto aumenta;
- forte sensibilidade a poucos outliers;
- coeficientes instáveis quando variáveis são alteradas;
- uso de dados do futuro ou informação derivada do alvo;
- divisão aleatória em um problema temporal;
- extrapolação para valores fora da faixa observada;
- modelo mais complexo sem ganho consistente sobre o baseline.

## Estrutura esperada dos notebooks

Cada projeto pode evoluir nesta sequência:

- `01-problema-e-hipoteses.ipynb`
- `02-exploracao-e-baseline.ipynb`
- `03-modelo-e-avaliacao.ipynb`
- `04-diagnostico-e-comparacao.ipynb`
- `README.md` com a decisão final.

Não vamos começar pelo código. Primeiro vamos formular a pergunta, prever o comportamento esperado e definir como reconhecer uma resposta ruim.
