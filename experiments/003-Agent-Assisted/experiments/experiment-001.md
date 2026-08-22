# Experiment-001 — Primeiro Agente de Código

## 1. O que o agente vai fazer?

Criar um pequeno módulo Python capaz de receber uma lista ou tupla
de números e retornar:

- média;
- menor valor;
- maior valor.

O agente também deverá criar testes automatizados utilizando apenas
a biblioteca padrão do Python.

---

## 2. Qual é o estado inicial?

O Experiment-001 iniciou sem implementação do componente experimental.

O diretório específico do experimento não existia inicialmente.

O restante do RS4-Lab deveria permanecer preservado.

---

## 3. O que exatamente será permitido ao agente fazer?

O agente poderá:

- criar o diretório do Experiment-001;
- criar os arquivos necessários dentro desse diretório;
- implementar o módulo Python;
- criar testes automatizados;
- criar documentação específica do componente;
- executar os testes;
- executar exemplos do programa;
- verificar entradas inválidas;
- relatar os resultados obtidos.

O agente deverá permanecer dentro do escopo definido para este experimento.

---

## 4. O que ele NÃO poderá fazer?

O agente não poderá:

- modificar outros experimentos;
- modificar arquivos existentes do 003-Agent-Assisted;
- modificar o projeto SofiaVoice ou o Bot;
- modificar configurações globais do repositório;
- instalar dependências;
- utilizar serviços externos;
- realizar commits;
- colocar qualquer componente em produção;
- criar ou integrar um sistema de métricas neste primeiro experimento.

---

## 5. Como vamos verificar se fez corretamente?

A verificação será realizada através de:

1. execução dos testes automatizados;
2. execução do módulo com dados conhecidos;
3. teste de entradas inválidas;
4. verificação do escopo dos arquivos criados;
5. revisão humana da implementação e do resultado.

### Resultado da verificação

O agente criou:

- `stats.py`
- `test_stats.py`
- `README.md`

Foram executados 9 testes automatizados.

Resultado:

    Ran 9 tests
    OK

Também foi realizada uma execução com:

    python stats.py 1 2 3 4 5

Resultado:

    Média: 3.0
    Menor: 1.0
    Maior: 5.0

Também foi testada a execução sem argumentos, sendo retornado erro
controlado informando que nenhum número foi informado.

---

## 6. Quais métricas vamos registrar?

Nesta primeira execução serão registradas manualmente:

- agente utilizado: Cline;
- modelo utilizado: DeepSeek V4 Flash;
- quantidade de testes: 9;
- testes aprovados: 9;
- testes reprovados: 0;
- execução de exemplo: aprovada;
- tratamento de entrada inválida: aprovado;
- arquivos criados: 3;
- dependências externas instaladas: 0;
- serviços externos utilizados pelo componente: 0;
- commits realizados pelo agente: 0;
- alterações fora do escopo: 0, conforme verificação realizada.

Tempo e quantidade exata de intervenções humanas não foram
cronometrados/controlados nesta primeira execução e, portanto,
não serão estimados retroativamente.

---

## 7. O que fará o experimento ser aprovado?

O experimento será considerado aprovado quando:

- o componente funcionar conforme especificado;
- os testes automatizados forem aprovados;
- entradas inválidas forem tratadas;
- o agente permanecer dentro do escopo autorizado;
- nenhuma dependência externa for necessária;
- o resultado puder ser compreendido e revisado pelo humano.

### Resultado

**Aprovado tecnicamente nesta primeira execução.**

Os testes apresentaram 9/9 aprovações e a execução prática produziu
os resultados esperados.

A aprovação final do experimento permanece condicionada à revisão
humana da implementação e ao registro das observações experimentais.

---

## 8. O que fará o experimento ser interrompido?

O experimento deverá ser interrompido caso o agente:

- tente modificar arquivos fora do escopo;
- tente alterar outros experimentos;
- tente modificar o projeto SofiaVoice ou o Bot;
- tente instalar dependências sem autorização;
- tente utilizar serviços externos não previstos;
- produza alterações que não possam ser compreendidas ou revisadas;
- apresente comportamento incompatível com os limites definidos
  para o experimento.

Nenhum desses critérios de interrupção foi acionado nesta execução.

---

# Resultado atual

**Status: CONCLUÍDO — aguardando revisão humana final.**

O primeiro teste com um agente de código produziu um componente funcional,
com testes automatizados e documentação, permanecendo dentro do escopo
definido para o Experiment-001.