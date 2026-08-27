# Notas — Experiment-003 — Agent-Assisted

## Primeira execução

O primeiro agente de código utilizado no experimento Agent-Assisted foi o Cline, utilizando o modelo DeepSeek V4 Flash.

A tarefa escolhida foi deliberadamente pequena e controlada: criar um módulo Python capaz de calcular a média, o menor e o maior valor de uma coleção de números.

A escolha de uma tarefa simples teve como objetivo reduzir a complexidade do experimento e permitir a observação do comportamento do agente em uma situação facilmente verificável.

Antes da execução, o agente foi instruído a apresentar um plano e recebeu limites explícitos de escopo.

### Execução observada

Durante a execução, o agente:

* criou o diretório específico do experimento;
* criou `stats.py`;
* criou `test_stats.py`;
* criou `README.md`;
* executou testes automatizados;
* realizou uma demonstração prática;
* verificou entradas inválidas;
* não instalou dependências;
* não utilizou serviços externos;
* não realizou commits.

### Intervenção humana

Durante a execução, o agente tentou utilizar `&&` em um comando destinado ao PowerShell.

O comando não era adequado ao ambiente utilizado. O problema foi identificado durante a execução e o agente adaptou o comando para `;`.

A ocorrência foi registrada como uma intervenção de ambiente, não como falha na lógica do código produzido.

### Observações

O agente apresentou comportamento compatível com a hipótese inicial do experimento: atuar como operador dentro de um escopo previamente definido, executando tarefas e aguardando orientação quando necessário.

A tarefa também permitiu observar que a supervisão humana continua relevante mesmo em atividades de baixo risco, especialmente para decisões relacionadas ao ambiente, escopo e validação do resultado.

O objetivo desta primeira execução não era produzir um componente sofisticado, mas estabelecer uma situação pequena, controlada e verificável para observar:

* capacidade de execução;
* necessidade de intervenção humana;
* comportamento diante de erros;
* qualidade do resultado;
* capacidade de seguir restrições;
* relação entre autonomia e supervisão.

### Relação com as métricas

Os dados quantitativos desta execução devem ser registrados separadamente na estrutura `metrics/benchmarks/`.

Este arquivo registra principalmente observações qualitativas e acontecimentos relevantes durante o experimento.

### Resultado inicial

Esta execução servirá como referência inicial para os próximos experimentos Agent-Assisted.

Os resultados não devem ser utilizados isoladamente para concluir que agentes são superiores à execução manual. A comparação deverá considerar tempo, qualidade, erros, retrabalho, necessidade de intervenção e nível de entendimento do operador.

O objetivo do RS4 é medir o efeito da utilização do agente, e não assumir previamente que sua utilização representa uma melhoria.
