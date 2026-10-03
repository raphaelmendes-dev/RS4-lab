<div align="center">
<img src="https://raw.githubusercontent.com/raphaelmendes-dev/sofiavoice/main/assets/Rs4Machine.png" alt="Rs4Machine Logo" width="180" />

# 🧪 RS4 Lab

**Laboratório de Sistemas Experimentais · Rs4Machine**

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Experimentação%20ativa-blue)

> Experimentar primeiro. Medir. Compreender. Somente então escalar.

</div>

---

## O que RS4 Lab faz hoje

RS4 Lab é a camada de execução e evidência do programa de pesquisa da Rs4Machine. O repositório está atualmente focado em experimentação controlada de sistemas de IA, orquestração de agentes, medição de latência e workflows de validação orientados à produção.

O trabalho ativo não é uma corrida de entrega de produto; é um laboratório prioritário de medição para validar hipóteses sob condições controladas. O foco atual está em:

- benchmarking de pipelines de IA e agentes sob condições repetíveis;
- validação de orquestração end-to-end sob execução local;
- rastreamento de latência, status e geração de artefatos por nó ou estágio;
- transformar experimentos em evidência rastreável, não em decisões guiadas por intuição.

O trabalho mais recente está concentrado nas trilhas `experiments/005-ai-system-improvement` e `experiments/006-cortex-flow`, com um movimento claro de mapeamento de baseline de arquitetura para avaliação de multi-agentes e captura de telemetria.

---

## Status atual do projeto

O repositório está em uma fase de pesquisa e validação ativa.

Sinais recentes do código:

- `experiments/005-ai-system-improvement/001-sofiavoice/` documenta o caminho de lançamento do SofiaVoice v2.0, incluindo comparações de benchmark de latência e relatórios de execução.
- `experiments/006-cortex-flow/` é o experimento de orquestração ativo. Seu ramo v2.0.0 inclui métricas por agente, testes de integração e artefatos de validação consolidados.
- A estrutura do repositório é organizada em torno de pastas de experimento, não em um layout de aplicação monolítica.
- A telemetria é capturada como métricas JSON e relatórios Markdown em vez de uma camada de processamento global única.

Um diretório de `Metrics/` no nível do repositório não é a estrutura organizacional principal atual; a telemetria recente é armazenada dentro das próprias pastas de experimento, especialmente em `experiments/006-cortex-flow/v2.0.0/`.

---

## Estrutura do repositório

```text
.
├── LICENSE
├── README.md
├── README.pt-BR.md
├── .gitignore
├── experiments/
│   ├── 001-architeture-first/
│   ├── 002-pipeline-validation/
│   ├── 003-Agent-Assisted/
│   ├── 004-local-triage-automation/
│   ├── 005-ai-system-improvement/
│   │   └── 001-sofiavoice/
│   ├── 006-cortex-flow/
│   │   ├── README.md
│   │   ├── v1.0.0/
│   │   └── v2.0.0/
│   │       ├── 00-metrics_setup_v2.json
│   │       ├── 01-metrics_chroma_v2.json
│   │       ├── ...
│   │       ├── 11-metrics_integracao_v2.json
│   │       ├── 12-metrics_agente7_evaluator_v2.json
│   │       ├── 13-metrics_triagem_v2.json
│   │       ├── implementation-tests-agents/
│   │       └── drafts/
│   └── 007-commerce-pipeline/
└── docs/ (conforme necessário pelos experimentos)
```

### Trilhas principais de experimento

- `experiments/001-architeture-first/` — baseline de arquitetura e mapeamento de gargalos.
- `experiments/002-pipeline-validation/` — overview de pipeline e notas de validação.
- `experiments/003-Agent-Assisted/` — experimentos assistidos por agentes e validação estatística.
- `experiments/004-local-triage-automation/` — estudos de automação de triagem.
- `experiments/005-ai-system-improvement/001-sofiavoice/` — benchmarking SofiaVoice, evidência de lançamento e comparações de latência.
- `experiments/006-cortex-flow/` — experimento de orquestração multi-agente atual com validação rica em telemetria.
- `experiments/007-commerce-pipeline/` — experimentos de pipeline orientados a comércio e artefatos de resultado.

---

## Suíte de métricas e validação implementada

O repositório atualmente usa um modelo de medição em camadas baseado em artefatos e evidência, não apenas scripts de execução.

### Modelo de medição

- snapshots de métricas JSON por nó;
- relatórios de integração end-to-end em Markdown;
- compilação validada de arquivos Python modificados;
- rastreamento de execução de agente com timestamps e campos de status;
- verificação em nível de rota para fluxos de orquestração.

### Padrão de telemetria atual

O experimento mais recente (`experiments/006-cortex-flow/v2.0.0/`) segue este padrão:

- `00-metrics_setup_v2.json` a `13-metrics_triagem_v2.json` — métricas por estágio do fluxo de orquestração;
- `11-metrics_integracao_v2.json` — resultado de integração end-to-end consolidado;
- `implementation-tests-agents/` — scripts Python que exercem nós de agentes e o pipeline completo;
- `drafts/` — avaliações, ofertas, sínteses refinadas e rascunhos de template produzidos durante a execução;
- `Result_*.md` e artefatos relacionados em outros experimentos para relatórios de execução.

Este setup fornece rastreabilidade para:

- status de execução do nó;
- latência por estágio;
- timing total do pipeline;
- validação de existência e conteúdo de artefato;
- regressão e comparação entre versões de experimento.

---

## Estrutura recente de teste e execução

O trabalho mais recente do Cortex Flow inclui uma suíte de scripts de validação sob:

```text
experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/
├── 01-test_nodo0.py
├── 02-test_nodo1.py
├── 03-test_nodo_redator.py
├── 04-test_nodo_techscout.py
├── 05-test_nodo_critico.py
├── 06-test_nodo_sintetizador.py
├── 07-test_nodo_builder.py
├── 08-test_nodo_builder.py
├── 09-test_esteira_completa.py
```

Estes scripts validam:

- execução em nível de nó;
- sequência de roteamento e transições de estado;
- validação de sintaxe e compile-time;
- integração do pipeline completo;
- geração e persistência de artefatos de métricas para comparação posterior.

---

## Como executar os scripts de teste

Use a raiz do repositório como diretório de trabalho.

### 1) Executar um script de validação único

```bash
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py
```

Isto executa a validação de rota integrada completa, coleta métricas JSON e escreve o relatório de integração consolidado.

### 2) Executar uma variante específica de rota

```bash
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py A
python experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/09-test_esteira_completa.py B
```

O script aceita a seleção de rota no workflow de validação e mescla os resultados no mesmo arquivo de métricas sem alterar a lógica de execução principal.

### 3) Validar sintaxe e saúde básica do projeto

```bash
python -m py_compile \
  experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/01-test_nodo0.py \
  experiments/006-cortex-flow/v2.0.0/implementation-tests-agents/02-test_nodo1.py
```

### 4) Usar pytest quando a pasta alvo contém verificações no estilo de unidade

```bash
pytest experiments/003-Agent-Assisted/
```

Este repositório é primariamente organizado em torno de scripts de experimento e saída de evidência, então o padrão de execução dominante é invocação direta em Python dos arquivos de validação em vez de um único runner global.

---

## Padrões de execução

RS4 Lab segue uma disciplina experimental rigorosa:

- verificar uma hipótese antes de escalar;
- manter evidência perto da execução;
- preferir métricas reproduzíveis a afirmações qualitativas;
- manter artefatos de teste auditáveis;
- manter a responsabilidade humana em decisões críticas.

---

## Status

O projeto está em uma fase experimental ativa focada em medição, validação de orquestração e geração de evidência de agentes.

O estado atual do repositório reflete uma transição de documentação de arquitetura para experimentação guiada por métricas, com o material recente mais maduro em:

- `experiments/005-ai-system-improvement/001-sofiavoice/`
- `experiments/006-cortex-flow/v2.0.0/`

---

## Autor

**Raphael Mendes**

**AI Systems Engineer · Rs4Machine**

> A tecnologia pode ampliar nossa capacidade. Ela não deve substituir nossa responsabilidade.
