Eu sugiro que o 001-sofiavoice tenha inicialmente quatro dimensões:

Funcionalidade — a Sofia responde corretamente?
Latência — quanto tempo leva?
Confiabilidade — o comportamento é consistente em várias chamadas?
Falhas — o que acontece quando algo dá errado?

E só depois podemos investigar coisas como:

streaming;
chunking;
STT;
LLM;
TTS;
comunicação frontend ↔ backend;
gargalos.

Ou seja, não vamos assumir que streaming é a solução antes de descobrir onde está o problema.