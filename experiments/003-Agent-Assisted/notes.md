# Notas — Experiment-001

## Primeira execução

O primeiro agente de código utilizado no 003-Agent-Assisted foi o Cline,
utilizando o modelo DeepSeek V4 Flash.

A tarefa escolhida foi deliberadamente pequena: criar um módulo Python
para calcular média, menor e maior valor de uma coleção de números.

O agente foi obrigado a apresentar o plano antes da execução e recebeu
limites explícitos de escopo.

Durante a execução:

- criou o diretório específico do experimento;
- criou `stats.py`;
- criou `test_stats.py`;
- criou `README.md`;
- executou 9 testes automatizados;
- obteve 9/9 testes aprovados;
- executou uma demonstração real;
- verificou entrada inválida;
- não instalou dependências;
- não utilizou serviços externos;
- não realizou commits.

Observação importante:

O objetivo desta primeira tarefa não era produzir um componente
sofisticado, mas observar o comportamento do agente em uma tarefa
pequena, controlada e verificável.

Também foi possível observar uma necessidade de intervenção humana
quando o agente tentou utilizar `&&` em PowerShell. O agente identificou
o problema e adaptou o comando para `;`.

Essa execução servirá como referência inicial para experimentos futuros.