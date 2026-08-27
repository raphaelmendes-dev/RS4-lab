# Experiment-001 — Local Triage Automation

**Projeto:** RS4-Lab
**Linha experimental:** 004 — Local Triage Automation
**Status:** Especificação em elaboração
**Data:** 26/08/2026

---

## 1. Objetivo

Investigar se um modelo de linguagem local, executado através do Ollama e orquestrado por Python, pode auxiliar na triagem de documentos locais, reduzindo o tempo necessário para compreender cada arquivo e mantendo a decisão e a autorização da movimentação exclusivamente sob controle humano.

O experimento não pretende substituir a decisão humana.

O sistema deverá:

1. localizar os arquivos;
2. ler e extrair seu conteúdo;
3. utilizar o modelo local para interpretar o conteúdo;
4. apresentar um resumo breve ao operador;
5. aguardar a decisão humana;
6. executar somente a ação autorizada.

---

## 2. Hipótese

Um sistema composto por Python + Ollama + modelo de linguagem local pode auxiliar na triagem de arquivos não estruturados, fornecendo resumos suficientemente úteis para que o operador humano tome uma decisão de forma mais rápida, sem retirar do humano o controle sobre o destino final dos arquivos.

---

## 3. Princípio de autoridade

A IA pode:

* ler;
* interpretar;
* resumir;
* apresentar informações.

A IA **não pode decidir o destino do arquivo**.

A decisão pertence exclusivamente ao operador humano.

Fluxo:

```text
Arquivo
   ↓
Python
   ↓
Extração
   ↓
Ollama + modelo local
   ↓
Resumo
   ↓
Raphael
   ↓
S / N / Q
   ↓
Python executa a ação autorizada
```

---

## 4. Princípio de contenção

Nenhum arquivo será excluído permanentemente pelo sistema.

As ações possíveis são:

### S — Aprovar

Mover o arquivo para:

`_APROVADOS`

### N — Não aprovar

Mover o arquivo para:

`_LIXEIRA_DESKTOP`

A pasta `_LIXEIRA_DESKTOP` funciona como área de contingência para posterior revisão ou limpeza manual.

### Q — Interromper

Interromper o experimento.

O arquivo atualmente apresentado não deve ser movimentado.

O sistema deve possuir uma forma clara de interrupção durante a execução.

---

## 5. Área de trabalho

Os arquivos utilizados no experimento permanecerão fora do repositório Git.

Estrutura operacional:

```text
Área de Trabalho/
│
├── _TRIAGEM_RAIZ/
├── _APROVADOS/
└── _LIXEIRA_DESKTOP/
```

O Python deverá procurar os arquivos dentro de:

`_TRIAGEM_RAIZ`

Os arquivos aprovados serão enviados para:

`_APROVADOS`

Os arquivos não aprovados serão enviados para:

`_LIXEIRA_DESKTOP`

---

## 6. Tipos de arquivo

Para o primeiro piloto serão considerados:

* `.doc`
* `.docx`
* `.md`
* `.txt`

PDF não fará parte do primeiro piloto.

A inclusão de outros formatos poderá ser investigada posteriormente em outro experimento ou extensão controlada.

---

## 7. Fluxo operacional

### Etapa 1 — Varredura

O Python localiza os arquivos existentes em `_TRIAGEM_RAIZ`.

Nenhum arquivo deve ser movimentado nessa etapa.

### Etapa 2 — Leitura e extração

O sistema obtém o conteúdo necessário para análise.

A estratégia de extração deverá respeitar o tipo de arquivo.

### Etapa 3 — Interpretação

O conteúdo extraído é enviado ao Ollama para análise pelo modelo local.

O objetivo é obter uma síntese curta contendo os conceitos centrais do documento.

### Etapa 4 — Apresentação

O terminal apresenta ao operador:

* nome do arquivo;
* resumo produzido;
* localização do arquivo;
* opções de decisão.

Exemplo:

```text
Arquivo: exemplo.docx

Resumo:
Documento relacionado a um projeto de automação
utilizando IA e n8n.

[S] Aprovar
[N] Não aprovar
[Q] Interromper
```

### Etapa 5 — Decisão humana

Raphael escolhe:

```text
S
N
Q
```

O modelo não realiza essa escolha.

### Etapa 6 — Execução

Após a decisão:

```text
S → _APROVADOS
N → _LIXEIRA_DESKTOP
Q → interromper
```

---

## 8. Métricas

O experimento utilizará inicialmente quatro métricas principais.

### M1 — Tempo

Registrar o tempo de cada execução.

Serão registrados dois tempos diferentes.

#### Tempo de processamento da máquina

Definição:

> Do início da leitura do arquivo até o resumo estar pronto para ser apresentado ao humano.

Esse tempo será medido automaticamente pelo Python.

#### Tempo de decisão humana

Definição:

> Do momento em que o resumo é apresentado ao operador até a resposta `S`, `N` ou `Q`.

Também deverá ser registrado automaticamente.

---

### M2 — Qualidade do resumo

Escala humana de 0 a 3:

| Nota | Significado          |
| ---- | -------------------- |
| 0    | Incorreto            |
| 1    | Pouco útil           |
| 2    | Adequado             |
| 3    | Preciso e suficiente |

A avaliação será realizada pelo operador humano.

A qualidade do resumo não representa a decisão S/N.

São avaliações diferentes.

---

### M3 — Volume processado

Registrar:

* quantidade total de arquivos processados;
* quantidade de aprovados;
* quantidade de não aprovados;
* quantidade de interrupções.

---

### M4 — Erros

Registrar ocorrências como:

* erro de leitura;
* erro de extração;
* erro do modelo;
* arquivo incompatível;
* falha de movimentação;
* interrupção;
* qualquer outro erro relevante.

---

## 9. Registro das evidências

As métricas produzidas durante a execução deverão ser armazenadas em:

`metrics.json`

O arquivo deverá registrar os dados reais da execução para permitir análise posterior.

O formato detalhado do JSON será definido antes da implementação.

---

## 10. Baseline

Antes da utilização da IA foi realizada uma triagem manual.

Resultado do baseline:

* arquivos processados: 6;
* aprovados: 4;
* não aprovados: 2;
* tempo total: 183 segundos;
* tempo médio: 30,5 segundos por arquivo.

A amostra real foi composta por:

* 3 arquivos Word inicialmente;
* 1 arquivo Markdown;
* 1 arquivo TXT;
* 1 arquivo Word.

O baseline representa a condição de referência para comparação com a triagem assistida por IA.

O resultado não deve ser tratado como meta nem como conclusão sobre eficiência.

---

## 11. Comparação

A comparação deverá considerar:

```text
BASELINE MANUAL

leitura
   ↓
compreensão
   ↓
decisão

vs.

TRIAGEM ASSISTIDA

leitura / extração
   ↓
Ollama
   ↓
resumo
   ↓
decisão humana
```

A análise deverá considerar separadamente:

* tempo de processamento da máquina;
* tempo de decisão humana;
* tempo total;
* qualidade do resumo;
* volume processado;
* erros.

---

## 12. Critério de controle

O experimento não será considerado bem-sucedido apenas porque o sistema funciona tecnicamente.

A avaliação deverá considerar simultaneamente:

1. utilidade do resumo;
2. tempo;
3. ausência de perda inadvertida de dados;
4. manutenção da decisão humana;
5. possibilidade de interrupção;
6. funcionamento correto da movimentação autorizada.

O experimento deve produzir evidências suficientes para decidir se a abordagem merece uma próxima etapa.

---

## 13. Escopo do primeiro piloto

O primeiro piloto será pequeno.

Objetivos:

* verificar se os arquivos podem ser processados;
* verificar a extração de conteúdo;
* verificar a comunicação com o Ollama;
* verificar a qualidade dos resumos;
* verificar a interface S/N/Q;
* verificar a movimentação controlada;
* verificar a coleta das métricas;
* verificar a interrupção segura.

Não haverá tentativa de escalar o sistema antes da análise dos resultados do piloto.

---

## 14. Fora do escopo

Não faz parte deste experimento:

* exclusão automática de arquivos;
* decisão automática de aprovação ou descarte;
* processamento de PDF;
* integração com Obsidian;
* integração com NotebookLM;
* automação em grande escala;
* construção de uma plataforma completa;
* execução remota;
* envio dos documentos para APIs externas.

---

## 15. Estado

**Baseline:** concluído.

**Especificação:** em elaboração.

**Implementação:** não iniciada.

**Teste piloto:** não iniciado.

**Métricas do sistema:** ainda não coletadas.

---

## 16. Próximo passo

Antes da implementação, revisar e aprovar esta especificação.

Após aprovação:

1. definir o modelo local;
2. definir a estratégia de extração para os formatos aceitos;
3. definir o formato final de `metrics.json`;
4. implementar a primeira versão;
5. executar o piloto;
6. verificar os resultados;
7. registrar as evidências;
8. comparar com o baseline.

**Regra do experimento:**

> Primeiro definir o que o sistema deve fazer.
> Depois implementar.
> Depois medir.
> Depois interpretar.
