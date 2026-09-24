# Experiment 002 — Pipeline Validation

## Date

21/08/2026

## Objective

Validate the operation of SofiaVoice's audio pipeline in a local environment, from audio input to response generation and output audio.

## Environment

- Python 3.14.2
- FastAPI
- Uvicorn
- Groq API
- Whisper Large V3
- openai/gpt-oss-20b
- gTTS

## Procedure

1. Rebuilt the backend virtual environment.
2. Installed dependencies.
3. Configured the `GROQ_API_KEY` environment variable.
4. Initialized the FastAPI server.
5. Validated the `/health` endpoint.
6. Ran individual tests on `/api/chat` and `/api/speak`.
7. Tested the end-to-end pipeline via `/api/voice`.

## Issue Encountered

The previously configured model:

`llama-3.3-70b-versatile`

returned a `model_not_found` error.

Model availability was checked directly via the Groq API.

## Changes Made

The LLM service was updated to:

`openai/gpt-oss-20b`

Following this change, the endpoint resumed processing requests normally.

## Results

The end-to-end pipeline was successfully validated.

Flow:

AUDIO → STT → LLM → TTS → BASE64

The `/api/voice` endpoint returned HTTP 200 and delivered:

- Transcribed text;
- LLM-generated response;
- Base64-encoded MP3 audio.

## Observations

During testing, occasional inaccurate transcriptions and empty responses were observed for certain audio inputs. Subsequent tests with clearer, longer audio clips yielded consistent results.

This suggests that input audio quality and duration may impact STT stability, though this hypothesis requires controlled testing.

## Conclusion

SofiaVoice's primary pipeline is functional in a local environment.

The next step is to validate full frontend integration, followed by latency benchmarking and bottleneck identification.

## Next Experiment

Investigate frontend → backend integration and establish baseline metrics for STT, LLM, TTS, and total pipeline execution time.