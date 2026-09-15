# Experimento 001 - Arquitetura da SofiaVoice

> 🧊 **REGISTRO HISTÓRICO CONGELADO — Baseline v1.0 (Síncrono Legado)**
> Este documento descreve o estado de referência **v1.0** e NÃO deve ser alterado retroativamente.
> A transição para o pipeline assíncrono v2.0 está registrada em
> [`experiments/005-ai-system-improvement/001-sofiavoice/`](../005-ai-system-improvement/001-sofiavoice/).

**Data:** 19/08/2026  
**Objetivo:** Mapear arquitetura atual da SofiaVoice e identificar gargalos.

## Arquitetura Atual (baseline v1.0)
- **Frontend:** Next.js (captura áudio via Web Audio API)
- **Backend:** FastAPI (roda no Render)
- **STT:** Whisper (via Groq)
- **LLM:** LLaMA 3.3 70B (via Groq)
- **TTS:** gTTS (salva arquivo, converte para base64)

## Gargalos Identificados
1. TTS salva arquivo em disco → latência extra
2. Pipeline sequencial (um passo espera o outro)
3. Múltiplas idas e voltas HTTP

## Próximo Passo
- [ ] Criar painel de métricas para medir cada etapa
- [ ] Testar Web Speech API como alternativa ao gTTS
- [ ] Implementar streaming de áudio (chunking)