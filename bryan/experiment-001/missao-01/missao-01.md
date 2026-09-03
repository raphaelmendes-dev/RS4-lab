# RS4 MACHINE | AI RESEARCH LAB
## Experiment-001 · Missão 01 — Construir seu Portfólio de Apresentação
 
---
 
## 0. ANTES DE QUALQUER COISA
 
1. Leia `../filosofia.md` (se ainda não leu).
2. Preencha `baseline.md` — **sem pular**. É lá que você registra suas ideias antes de qualquer IA opinar.
Só depois disso, volte pra cá.
 
---
 
## 1. O QUE É ESSA MISSÃO
 
Você vai construir seu próprio portfólio de apresentação — o site que vai te representar tecnicamente. Não é um teste, é o seu primeiro artefato real dentro do RS4Machine.
 
Você **não** vai copiar nada do que está aqui. O material abaixo é referência — o mesmo papel que teve pra mim quando comecei sem saber programar: mostrar que dá pra construir algo com identidade forte tendo a IA como parceira de raciocínio, não como "geradora mágica" de coisa pronta.
 
**O que importa no final não é o quão parecido ficou com os exemplos. É o quanto tem de você.**
 
---
 
## 2. MATERIAL DE REFERÊNCIA
 
### 2.1 Design System do RS4Machine (paleta e componentes)
- Background: preto profundo / grafite escuro (`#0a0a0a`, `#0d1117`)
- Texto principal: branco acinzentado (`#e0e0e0`) · Texto secundário: cinza médio (`#888888`)
- Tipografia: **Mono** (JetBrains Mono, Fira Code, Space Mono) para títulos/dados — passa a ideia de engenharia. **Sans-serif** limpa (Inter, Roboto) para texto corrido.
- Efeito neon sutil (`box-shadow`/`text-shadow`) em elementos interativos.
- Componentes reutilizáveis: `.rs4-button-neon` (borda neon, pulso no hover), `.rs4-card` (fundo `#161b22`, borda sutil), `.rs4-input` (acende em neon ao focar), `.rs4-badge` (tag de status).
Isso é o "DNA visual" da marca RS4. Seu portfólio pode se inspirar nele — mas você não é obrigado a usar essa paleta exata se sua resposta na pergunta 2/13 do baseline apontar outra direção. A identidade RS4 é um ponto de partida, não uma prisão.
 
### 2.2 Exemplo de componente — Sofia Voice (Status Widget)
Um exemplo real de como um componente pequeno pode ter muita identidade: um círculo/onda central que "pulsa" simulando fala, e um badge que muda de cor conforme o estado (Verde = Ouvindo, Azul = Processando, Roxo = Falando). Mostra como algo simples — um indicador de status — pode carregar a estética inteira do projeto.
 
### 2.3 Exemplo de portfólio em produção (RS4Machine)
`https://portfolio-modular-rs4-machine.vercel.app/`
 
Isso é o **meu** portfólio, construído com esse mesmo método (jogar material na IA, refinar, decidir, construir). Não é modelo pra copiar estrutura ou texto — é prova de até onde esse processo consegue chegar quando bem conduzido. Repare como cada seção (Sobre, Projetos, Visão, Stack, Contato) tem uma frase de identidade — isso é algo que você também vai precisar definir pro seu.
 
---
 
## 3. O PIPELINE — 4 AGENTES DE REFINO
 
Essa é a mesma lógica usada nos projetos do RS4: você não pede pra uma única IA "fazer o portfólio". Você passa a ideia por **camadas de refino**, cada uma com um papel diferente. Isso te obriga a pensar criticamente sobre a sua própria ideia, em vez de aceitar a primeira resposta que aparece.
 
```
Você (baseline) 
   ↓
AGENTE 1 — ChatGPT      → Análise Estrutural
   ↓
AGENTE 2 — Perplexity   → Sugestão de Melhoria
   ↓
AGENTE 3 — Grok         → Crítica Técnica
   ↓
AGENTE 4 — Claude       → Plano Consolidado + Construção + Validação
```
 
Você leva a saída de cada etapa pra próxima. No final, tudo desemboca aqui no Claude, que vai te ajudar a montar e validar o código de verdade.
 
---
 
### PROMPT INICIAL — Agente 1 (ChatGPT)
 
Copie e adapte com suas respostas do `baseline.md` antes de enviar:
 
```
Atue como um Designer de Produto e Arquiteto de Sistemas Sênior.
 
Estou construindo meu portfólio de apresentação pessoal como estudante de TI
(SENAI, me preparando para vestibular na área) e membro iniciante de um
laboratório de IA aplicada (RS4Machine).
 
Aqui estão minhas respostas de baseline sobre estilo, cores e identidade:
[COLE AQUI SUAS RESPOSTAS DO baseline.md]
 
Aqui está o Design System de referência que devo considerar (não copiar
obrigatoriamente, mas levar em conta):
[COLE AQUI O TRECHO DO DESIGN SYSTEM DA SEÇÃO 2.1]
 
Não me dê sugestões ainda. Apenas analise minhas respostas e me devolva,
de forma estruturada:
1. Que direção visual essas respostas sugerem (paleta, tipografia, tom)
2. Que seções um portfólio pessoal como esse normalmente precisa ter
3. Onde minhas respostas têm contradição ou falta de clareza (se houver)
4. Que perguntas eu ainda não respondi e deveria pensar melhor
```
 
**O que fazer com a saída:** leia com calma, e se o Agente 1 apontar contradição ou pergunta que você não tinha pensado, responda ANTES de seguir pra próxima etapa. Não adianta acelerar o pipeline com uma base mal resolvida.
 
---
 
### AGENTE 2 (Perplexity) — Sugestão de Melhoria
 
```
Com base nesta análise estrutural do meu portfólio pessoal:
[COLE A SAÍDA DO AGENTE 1]
 
Pesquise boas práticas de mercado para portfólios de devs/estudantes de TI
em 2026. Sugira estrutura de seções, bibliotecas ou recursos visuais que
tornem esse portfólio mais forte — mas sem me tirar da identidade que já
apareceu na análise anterior. Foque em "o que pode tornar isso excepcional
sem descaracterizar quem eu sou".
```
 
---
 
### AGENTE 3 (Grok) — Crítica Técnica
 
```
Recebi este plano de portfólio pessoal [COLE SAÍDAS DO AGENTE 1 E 2].
 
Esqueça o otimismo. Aja como um engenheiro sênior com humor ácido e
20 anos de experiência revisando portfólios de iniciantes.
 
Onde esse plano é genérico demais? Onde parece "mais um portfólio de IA
generativa" em vez de algo pessoal? O que vai ficar bonito mas oco?
Seja direto e não amacie a crítica só porque eu sou iniciante.
```
 
**Importante:** isso vai doer um pouco de propósito. Crítica dura sobre a ideia não é crítica sobre você. Leia, respire, e separe o que é ajuste válido do que talvez você discorde — você pode discordar do Agente 3 se tiver um motivo.
 
---
 
### AGENTE 4 (Claude) — Plano Consolidado, Construção e Validação
 
Esta etapa acontece aqui, comigo. Traga tudo:
 
```
Recebi uma análise estrutural, sugestões de melhoria e uma crítica técnica
sobre o portfólio pessoal que estou construindo (Missão 01 do RS4Machine).
 
[COLE AS 3 SAÍDAS ANTERIORES]
[COLE TAMBÉM SEU baseline.md ORIGINAL]
 
Quero que você consolide tudo isso em um plano técnico definitivo, e depois
me ajude a construir o esqueleto de código (HTML/CSS ou o que fizer mais
sentido para meu nível). No final, quero que você valide comigo se o
resultado é coerente com minhas respostas originais do baseline — e não
apenas com as sugestões das outras IAs.
```
 
Aqui é onde a decisão final volta pra você: se alguma sugestão das etapas anteriores não bate com quem você é (baseline), você tem o direito de dizer isso e ajustar.
 
---
 
## 4. DEPOIS DE CONSTRUÍDO — SUBINDO SEU TRABALHO
 
1. Crie uma branch a partir do repositório RS4-Lab: `missao-01/portfolio-bryan`
2. Coloque o código dentro da estrutura combinada com o Raphael (ele vai te indicar onde).
3. Abra um Pull Request explicando: o que você construiu, o que mudou do baseline pro resultado final, e o que foi decisão sua vs. sugestão das IAs.
4. Preencha `notes.md` nesta mesma pasta (crie o arquivo se ainda não existir) com:
```
Missão: 01
Hipótese inicial (do baseline): 
O que mudou entre o baseline e o resultado final:
O que funcionou:
O que não funcionou / erro encontrado:
Decisão que foi só sua (não veio de nenhuma IA):
Próximo passo sugerido:
```
 
---
 
## 5. CRITÉRIO DE ENTREGA
 
A missão está completa quando:
 
- [ ] `baseline.md` está preenchido (feito antes do resto)
- [ ] Você passou pelas 4 etapas (mesmo que tenha discordado de alguma sugestão — discordar com justificativa também conta)
- [ ] O resultado final segue uma identidade visual coerente (não precisa ser a paleta RS4 exata, mas precisa fazer sentido)
- [ ] Você consegue explicar, com suas palavras, pelo menos 2 decisões de design que foram suas
- [ ] O PR foi aberto no repositório
- [ ] `notes.md` está preenchido
Depois disso, o Raphael avalia e vocês decidem juntos o próximo passo.
 
---
 
*RS4 Machine | AI Research Lab*
*Experiment. Measure. Understand. Build responsibly.*
