# Experiment 002 — Pipeline Validation

## Data

21/08/2026

## Objetivo

Validar o funcionamento do pipeline de voz da SofiaVoice em ambiente local,
desde a entrada de áudio até a geração da resposta e do áudio de saída.

## Ambiente

- Python 3.14.2
- FastAPI
- Uvicorn
- Groq API
- Whisper Large V3
- openai/gpt-oss-20b
- gTTS

## Procedimento

1. Reconstrução do ambiente virtual do backend.
2. Instalação das dependências.
3. Configuração da variável `GROQ_API_KEY`.
4. Inicialização do servidor FastAPI.
5. Validação do endpoint `/health`.
6. Testes individuais de `/api/chat` e `/api/speak`.
7. Teste do pipeline completo através de `/api/voice`.

## Problema Encontrado

O modelo anteriormente configurado:

`llama-3.3-70b-versatile`

retornou erro `model_not_found`.

A disponibilidade de modelos foi consultada diretamente através da API da
Groq.

## Alteração

O serviço LLM foi atualizado para:

`openai/gpt-oss-20b`

Após a alteração, o endpoint voltou a processar as requisições normalmente.

## Resultado

O pipeline completo foi validado com sucesso.

Fluxo:

ÁUDIO → STT → LLM → TTS → BASE64

O endpoint `/api/voice` retornou HTTP 200 e apresentou:

- texto transcrito;
- resposta gerada pelo LLM;
- áudio MP3 convertido para Base64.

## Observações

Durante os testes foram observadas algumas transcrições incorretas e respostas
vazias em determinados áudios. Testes posteriores com áudio mais claro e
mais longo produziram resultados consistentes.

Isso indica que a qualidade e duração do áudio de entrada podem influenciar
a estabilidade do STT, mas essa hipótese ainda precisa de testes controlados.

## Conclusão

O pipeline principal da SofiaVoice está funcional em ambiente local.

A próxima etapa é validar a integração completa com o frontend e,
posteriormente, medir latência e identificar possíveis gargalos.

## Próximo Experimento

Investigar a integração frontend → backend e estabelecer métricas básicas
para STT, LLM, TTS e tempo total do pipeline.