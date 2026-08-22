# 003 — Agent-Assisted Development

Status: Hipótese em avaliação

Data de início: 22/08/2026

Projeto: RS4-Lab

---

## 1. HIPÓTESE

Um agente de IA pode aumentar a capacidade operacional de Rafael
na execução de tarefas técnicas delimitadas, reduzindo tempo e
esforço sem degradar significativamente:

- qualidade;
- controle;
- capacidade de compreensão;
- capacidade de teste;
- capacidade de depuração;
- aprendizado.

A utilização de agentes não representa uma mudança no método RS4.

O agente será tratado como um operador dentro do método.

---

## 2. OBJETIVO

Medir se a utilização de agentes de IA realmente aumenta a
capacidade operacional do RS4.

O objetivo não é provar que agentes são melhores.

O objetivo é produzir evidências que permitam decidir:

- ampliar o uso;
- limitar o uso;
- modificar a forma de utilização;
- ou interromper o experimento.

---

## 3. PRINCÍPIO CENTRAL

O RS4 continua sendo o método.

Rafael continua sendo o decisor final.

O agente executa dentro do escopo delegado.

Modelo:

RS4
↓
Rafael — decisão
↓
Tarefa delimitada
↓
Agente — execução
↓
Verificação
↓
Evidências
↓
Resultados
↓
Dados
↓
Análise
↓
Aprendizado
↓
Próxima decisão

O agente pode produzir informação, código, análise ou proposta.

A decisão continua sendo de Rafael.

---

## 4. DIVISÃO ENTRE LABORATÓRIO E PROJETO

### RS4-Lab

O laboratório é responsável por:

- hipótese;
- planejamento do experimento;
- protocolo;
- métricas;
- resultados;
- análise;
- aprendizados;
- decisões;
- histórico do experimento.

### Projeto real

O projeto utilizado no experimento é responsável pela execução.

No caso deste primeiro experimento, a SofiaVoice será o ambiente
de aplicação técnica.

O agente trabalhará no repositório da SofiaVoice quando receber
uma tarefa autorizada.

### Regra

O Lab decide e registra.

O projeto executa.

Os resultados retornam ao Lab.

---

## 5. ESTADO INICIAL — BASELINE

O baseline deste experimento utiliza o estado da SofiaVoice
validado durante a etapa anterior do laboratório.

Não será necessário repetir testes já realizados apenas para
recriar artificialmente o baseline.

O estado de referência deve ser identificado pelo commit e pela
documentação existente no momento em que o experimento for iniciado.

### Pipeline validado

Áudio
↓
STT — Whisper Large V3
↓
Texto
↓
LLM
↓
Resposta
↓
TTS — gTTS
↓
MP3
↓
Base64
↓
Frontend

O endpoint `/api/voice` foi validado localmente com HTTP 200.

### Alteração relevante do baseline

O modelo LLM foi alterado de:

llama-3.3-70b-versatile

para:

openai/gpt-oss-20b

A alteração ocorreu porque o modelo anterior retornava:

404 model_not_found

Esse estado passa a ser a referência histórica para os
experimentos seguintes.

---

## 6. ARQUITETURA DOS AGENTES

Os agentes são divididos conceitualmente em dois ambientes.

### RS4-LAB — Agentes técnicos

Funções possíveis:

- operador de código;
- operador de testes;
- operador de documentação;
- operador de pesquisa;
- operador de dados;
- operador de análise;
- operador de revisão.

Esses agentes existem principalmente para aumentar a capacidade
técnica e experimental do laboratório.

Fluxo:

CÓDIGOS
↓
DADOS
↓
TESTES
↓
RESULTADOS

---

### OPERAÇÕES — Agentes de capital

Funções futuras:

- agente de conteúdo;
- agente de distribuição;
- agente de monitoramento;
- agente de dados;
- agente de planejamento.

Esses agentes pertencem à frente operacional de faturamento.

Eles são protótipos de operadores de capital e não fazem parte,
neste momento, do primeiro experimento técnico.

Fluxo:

CONTEÚDO
↓
PRODUTO
↓
DISTRIBUIÇÃO
↓
RESULTADOS

---

## 7. PAPEL DOS AGENTES

Os agentes de IA executam dentro do escopo delegado.

Eles podem:

- escrever código;
- revisar código;
- testar código;
- pesquisar;
- coletar dados;
- organizar dados;
- analisar resultados;
- gerar documentação;
- produzir propostas.

Eles não podem:

- definir sozinhos a direção do projeto;
- assumir autoridade sobre o projeto;
- aprovar sozinhos uma alteração crítica;
- colocar uma alteração relevante em produção;
- substituir o entendimento de Rafael;
- decidir sozinhos que uma solução está correta.

---

## 8. PAPEL DE RAFAEL

Rafael permanece como:

- decisor;
- responsável pela autorização;
- supervisor;
- testador humano;
- responsável pelo entendimento;
- responsável pela decisão final;
- responsável pelo aprendizado obtido no experimento.

O objetivo da utilização de agentes é aumentar a capacidade
de Rafael, não criar dependência.

---

## 9. TESTADORES

A verificação será dividida em camadas.

### Testador 1 — Máquina

Verifica aquilo que pode ser verificado automaticamente.

Exemplos:

- testes automatizados;
- execução correta;
- respostas esperadas;
- erros;
- regressões;
- comportamento técnico.

---

### Testador 2 — Agente verificador

Um agente diferente do agente executor, quando possível,
recebe a função de tentar encontrar problemas.

Sua função não é provar que a solução está correta.

Sua função é tentar encontrar motivos para considerá-la incorreta,
incompleta ou frágil.

Pergunta principal:

"Como isso pode estar errado?"

---

### Testador 3 — Medição

Responsável por coletar e organizar as evidências do experimento.

Exemplos:

- tempo;
- erros;
- retrabalho;
- alterações;
- testes;
- intervenções humanas;
- resultado.

---

### Testador 4 — Humano

Rafael responde:

"Eu entendo o que foi feito e consigo assumir a responsabilidade
por isso?"

Escala:

0 — não entendo

1 — entendo parcialmente

2 — consigo explicar

3 — consigo explicar, testar e depurar

A pontuação de compreensão humana é uma métrica do experimento.

---

## 10. PROTOCOLO DO EXPERIMENTO

Cada tarefa experimental deverá seguir, sempre que possível:

1. Definir uma tarefa pequena e delimitada.
2. Registrar o estado inicial.
3. Definir o resultado esperado.
4. Definir quais ações o agente está autorizado a executar.
5. Executar a tarefa.
6. Realizar testes.
7. Procurar problemas.
8. Coletar evidências.
9. Registrar métricas.
10. Rafael revisar e compreender o resultado.
11. Rafael testar e, quando possível, depurar.
12. Registrar o resultado.
13. Registrar o aprendizado.
14. Tomar a próxima decisão.

Fluxo:

BASELINE
↓
AGENTE
↓
EXECUÇÃO
↓
VERIFICAÇÃO
↓
EVIDÊNCIAS
↓
MÉTRICAS
↓
RAFAEL ANALISA
↓
DECISÃO

---

## 11. MÉTRICAS

As principais métricas do experimento serão:

| Métrica | Objetivo |
|---|---|
| Tempo para concluir | Medir velocidade |
| Bugs introduzidos | Medir impacto na qualidade |
| Tempo de correção | Medir custo dos erros |
| Retrabalho | Medir esforço adicional |
| Quantidade de alterações | Medir volume produzido |
| Código alterado após revisão | Medir necessidade de intervenção |
| Testes executados | Medir cobertura da verificação |
| Intervenções humanas | Medir quanto Rafael precisou interferir |
| Compreensão de Rafael | Medir aprendizado e controle |
| Resultado final | Verificar se a tarefa atingiu o objetivo |

A velocidade isoladamente não determina sucesso.

Um agente que termina mais rápido, mas exige grande quantidade
de correções ou produz uma solução que Rafael não compreende,
não representa necessariamente ganho operacional.

---

## 12. CRITÉRIO DE APROVAÇÃO

O agente será considerado operacionalmente útil quando demonstrar
ganho de capacidade sem perda significativa de:

- qualidade;
- controle;
- aprendizado;
- compreensão;
- capacidade de depuração.

A aprovação não será baseada apenas em velocidade.

Os critérios quantitativos poderão ser refinados após os primeiros
ciclos de medição.

---

## 13. CRITÉRIOS DE INTERRUPÇÃO

O experimento deverá ser interrompido quando ocorrer, entre outros:

- ação fora do escopo autorizado;
- alteração não autorizada;
- perda de dados;
- impossibilidade de rollback;
- comportamento não compreendido;
- risco superior ao benefício;
- custo desproporcional;
- degradação significativa da qualidade;
- impossibilidade de verificar o resultado;
- perda de controle humano.

A interrupção faz parte do experimento.

Interromper não significa fracasso.

Significa produzir uma informação sobre os limites do sistema.

---

## 14. CONTENÇÃO

A contenção é princípio permanente do uso de agentes no RS4.

Regras:

1. Rafael permanece como decisor final.
2. Todo agente recebe apenas o escopo necessário.
3. Todo sistema autônomo deve poder ser interrompido.
4. Decisões críticas não são delegadas completamente.
5. O entendimento não pode ser terceirizado.
6. Planos de contingência fazem parte do experimento.
7. Quanto maior o impacto potencial da tarefa, maior deve ser
   a supervisão.
8. O princípio de menor privilégio deve ser aplicado sempre que
   tecnicamente possível.

Pergunta obrigatória antes de delegar:

"E se der errado?"

---

## 15. PRIMEIRA TAREFA EXPERIMENTAL

A primeira tarefa ainda não está definida.

Ela deverá ser:

- pequena;
- reversível;
- mensurável;
- de baixo risco;
- suficientemente técnica para permitir comparação;
- suficientemente simples para Rafael compreender o resultado.

A tarefa será definida antes da execução do agente.

---

## 16. ESCOLHA DA FERRAMENTA

A ferramenta do primeiro agente ainda não representa uma decisão
permanente do RS4.

A escolha deverá considerar:

- controle;
- transparência;
- custo;
- facilidade de uso;
- capacidade de rollback;
- escopo de permissões;
- qualidade da execução;
- capacidade de supervisão.

O primeiro agente será tratado como parte do experimento,
não como ferramenta definitiva do RS4.

---

## 17. RESULTADOS

### Execução

Data:

Tarefa:

Agente:

Modelo:

Tempo:

Intervenções humanas:

---

### Testes

Testes executados:

Falhas:

Correções:

Resultado:

---

### Compreensão humana

Pontuação Rafael:

0 — não entendo

1 — entendo parcialmente

2 — consigo explicar

3 — consigo explicar, testar e depurar

---

### Aprendizado

O que funcionou?

O que não funcionou?

O que aprendemos?

---

## 18. DECISÃO

Após cada ciclo:

[ ] Ampliar utilização

[ ] Repetir experimento

[ ] Limitar utilização

[ ] Alterar protocolo

[ ] Trocar ferramenta/modelo

[ ] Interromper utilização

[ ] Outra decisão:

Justificativa:

---

## 19. PRINCÍPIO DO EXPERIMENTO

Não assumimos que agentes são melhores.

Não assumimos que agentes são piores.

Testamos.

Medimos.

Analisamos.

Aprendemos.

Decidimos.

---

## 20. CICLO RS4

APRENDER
↓
FAZER
↓
MEDIR
↓
ERRAR
↓
CORRIGIR
↓
EVOLUIR

O agente existe dentro desse ciclo.

Ele não substitui o ciclo.

---

## STATUS

Hipótese em avaliação.

Próximo marco:

Definir a primeira tarefa experimental e executar o primeiro ciclo
controlado de Agent-Assisted Development.

---

## FIM — 003 Agent-Assisted Development