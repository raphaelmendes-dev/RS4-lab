# RS4 Lab

Laboratório experimental da **RS4 Machine**.

> Experimentar primeiro. Medir. Entender. Só então escalar.

---

## O que é o RS4 Lab

O RS4 Lab é um espaço de experimentação controlada em sistemas inteligentes, agentes de IA e engenharia de software.

Não é uma startup.

Não é um playground de agentes.

É um laboratório com método.

Aqui registramos hipóteses, executamos experimentos pequenos, coletamos evidências e decidimos com base em dados — mantendo o humano como decisor final.

---

## Princípios

1. O humano permanece como decisor final e responsável pelo resultado.

2. Todo sistema autônomo deve ter forma clara, rápida e documentada de ser interrompido.

3. Decisões críticas nunca são delegadas completamente a agentes.

4. O entendimento e a capacidade de depurar não podem ser terceirizados.

5. Planos de contingência fazem parte do método, não são opcionais.

6. Quanto maior o impacto potencial da tarefa, maior deve ser o nível de supervisão e restrição.

---

## Estrutura atual

```text
experiments/
├── 001-architecture-first
├── 002-pipeline-validation
├── 003-Agent-Assisted
└── 004-local-triage-automation

metrics/
docs/

Cada experimento possui sua própria documentação, evidências e métricas conforme a necessidade.

Experimentos
#	Nome	Status	Início
001	Architecture First	Concluído	Ago/2026
002	Pipeline Validation	Concluído	Ago/2026
003	Agent-Assisted Development	Hipótese em avaliação	22/08/2026
004	Local Triage Automation	Em experimentação	Ago/2026
Experiment-003 — Agent-Assisted Development

Primeiros experimentos com agentes atuando como operadores dentro de tarefas delimitadas.

O objetivo é observar capacidade de execução, necessidade de intervenção humana, qualidade do resultado e relação entre autonomia e supervisão.

Experiment-004 — Local Triage Automation

Experimento voltado à avaliação de modelos locais em uma tarefa de triagem de arquivos.

O experimento utiliza um baseline humano como referência e registra métricas de tempo e qualidade para comparação entre modelos.

Primeira bateria registrada com:

Llama 3.2 3B
Qwen 2.5 3B

Os resultados ainda são experimentais e não representam uma conclusão sobre superioridade da automação.

Modelo de trabalho

RS4 (método)

↓

Raphael — decisão

↓

Tarefa delimitada

↓

Agente — execução (dentro do escopo)

↓

Verificação (Testador 1 a 4)

↓

Evidências → Resultados → Dados

↓

Análise → Aprendizado

↓

Próxima decisão

Camadas de verificação
Testador 1 — Máquina (testes automatizados)
Testador 2 — Agente verificador
Testador 3 — Medição (métricas)
Testador 4 — Humano (escala de entendimento 0–3)
Sobre agentes

Os agentes executam dentro do escopo delegado.

Eles podem:

Escrever, revisar e testar código
Gerar documentação
Coletar e organizar dados
Produzir propostas

Eles não podem:

Definir a direção do projeto
Aprovar alterações críticas
Substituir o entendimento humano
Colocar alterações relevantes em produção sozinhos
Lado capital (futuro)

O laboratório técnico e o lado operacional (capital) caminham juntos, mas em ritmos diferentes.

Enquanto o Lab valida métodos e qualidade, o lado capital explorará formas de gerar receita com custo próximo de zero (afiliados, templates, automações, etc.).

O capital serve para dar estabilidade e condições de continuar o trabalho.

Não é o norte principal.

Status

🚧 Em construção

Experimentos iniciados em Agosto/2026.

Atualmente, o laboratório está avançando da documentação inicial para experimentos comparativos com métricas.

Autor

Raphael Mendes

RS4 Machine | AI Research Lab

“A tecnologia pode aumentar nossa capacidade.
Ela não deve substituir nossa responsabilidade.”