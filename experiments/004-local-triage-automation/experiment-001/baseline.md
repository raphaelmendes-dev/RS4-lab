# Baseline — Triagem Manual

## Objetivo

Registrar como uma tarefa de triagem de arquivos é executada sem auxílio de IA, criando uma referência para comparação com o experimento Agent-Assisted.

O baseline representa a condição atual de trabalho humano.

---

## Regra

A tarefa foi executada sem agente, LLM ou automação de decisão.

O humano abriu, leu e avaliou cada arquivo individualmente e decidiu se ele deveria ser:

* aprovado;
* descartado.

Nenhum arquivo foi excluído permanentemente durante o baseline.

Arquivos aprovados foram movidos para:

`_APROVADOS`

Arquivos descartados foram movidos para:

`_LIXEIRA_DESKTOP`

---

## Amostra

Quantidade planejada:

**5 arquivos**

Quantidade efetivamente executada:

**6 arquivos**

A amostra foi composta por arquivos reais do acervo que estava sendo triado.

Tipos encontrados na amostra:

* Word;
* Markdown;
* TXT.

A diferença entre a quantidade planejada e executada foi registrada como parte do experimento, sem repetição da medição.

---

## Procedimento

Para cada arquivo:

1. Registrar o início da análise.
2. Abrir e ler o conteúdo necessário para compreender o arquivo.
3. Decidir se o arquivo seria aprovado ou descartado.
4. Registrar o tempo gasto na análise.
5. Registrar a decisão.
6. Mover o arquivo para o destino correspondente.
7. Registrar observações relevantes.

---

## Resultado observado

### Arquivo 1

**Arquivo:** `etapa1..doc/.docx`
**Tempo:** 30 s
**Decisão:** S — Aprovado
**Destino:** `_APROVADOS`
**Conteúdo/observação:** Bot WhatsApp com n8n.

### Arquivo 2

**Arquivo:** `INT_ia.doc/.docx`
**Tempo:** 54 s
**Decisão:** S — Aprovado
**Destino:** `_APROVADOS`
**Conteúdo/observação:** MetaPrompt + estratégia para perfil técnico.

### Arquivo 3

**Arquivo:** `makedown.md`
**Tempo:** 19 s
**Decisão:** S — Aprovado
**Destino:** `_APROVADOS`
**Conteúdo/observação:** Projeto de simulação da faculdade UNIVESP sobre IA, referente ao primeiro semestre.

### Arquivo 4

**Arquivo:** `proposta_maltbot .doc/.docx`
**Tempo:** 13 s
**Decisão:** N — Não aprovado
**Destino:** `_LIXEIRA_DESKTOP`
**Conteúdo/observação:** Projeto de chatbot com IA e n8n relacionado a trabalho freelance.

### Arquivo 5

**Arquivo:** `resultado.txt`
**Tempo:** 24 s
**Decisão:** N — Não aprovado
**Destino:** `_LIXEIRA_DESKTOP`
**Conteúdo/observação:** Possíveis ferramentas gratuitas.

### Arquivo 6

**Arquivo:** `Como estruturar... ..doc/.docx`
**Tempo:** 43 s
**Decisão:** S — Aprovado
**Destino:** `_APROVADOS`
**Conteúdo/observação:** Documento relacionado à questão "para que vários templates?".

---

## Dados consolidados

| Métrica                 |  Resultado |
| ----------------------- | ---------: |
| Arquivos planejados     |          5 |
| Arquivos processados    |          6 |
| Aprovados               |          4 |
| Não aprovados           |          2 |
| Tempo total             |      183 s |
| Tempo total             | 3 min 03 s |
| Tempo médio por arquivo |     30,5 s |

### Distribuição

**Aprovados:** 4 de 6 — 66,7%

**Não aprovados:** 2 de 6 — 33,3%

---

## Observação sobre o tempo

O tempo de análise variou entre:

**13 s e 54 s por arquivo.**

A variação indica que o esforço de triagem não foi uniforme entre os documentos.

O arquivo `INT_ia..doc/.docx` apresentou o maior tempo de análise, com **54 segundos**.

O arquivo `proposta_maltbot..doc/.docx` apresentou o menor tempo de análise, com **13 segundos**.

Essa variação será considerada posteriormente na comparação com a triagem assistida por IA.

---

## Métricas do Baseline

### 1. Tempo por arquivo

Tempo decorrido durante a análise humana de cada arquivo.

Resultado observado:

**30,5 s/arquivo em média**

### 2. Tempo total

Tempo necessário para concluir a análise da amostra:

**183 segundos / 3 min 03 s**

### 3. Volume processado

**6 arquivos**

### 4. Distribuição das decisões

* Aprovados: **4**
* Não aprovados: **2**

### 5. Erros ou dificuldades

Nenhum erro técnico ou falha de movimentação foi registrado durante a execução do baseline.

---

## Controle dos arquivos

Os seis arquivos foram efetivamente movimentados após a decisão humana.

Destino dos aprovados:

`_APROVADOS`

Destino dos não aprovados:

`_LIXEIRA_DESKTOP`

Nenhum arquivo foi excluído permanentemente.

---

## Interpretação

O baseline estabelece uma referência inicial para a triagem manual.

Na condição observada, Raphael levou em média **30,5 segundos por arquivo** para analisar e decidir sobre a amostra de seis arquivos.

Esse resultado não representa uma meta nem uma conclusão sobre eficiência.

Ele será utilizado posteriormente para comparação com a triagem assistida por IA.

A decisão humana permanece como referência de controle do experimento.

---

## Pergunta para o próximo estágio

> A utilização de um modelo local pode reduzir o tempo necessário para compreender e triar os arquivos, mantendo a decisão e a autorização da movimentação exclusivamente sob controle humano?

---

## Status

**CONCLUÍDO — BASELINE EXECUTADO**

Próximo passo:

**Definir a especificação operacional do Experiment-001 do Local Triage Automation antes da implementação.**
