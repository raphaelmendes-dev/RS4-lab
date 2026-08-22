# Experiment-001 — Módulo de Estatísticas

## O que faz

Um pequeno módulo Python que recebe uma lista de números e retorna:

- a **média**;
- o **menor** valor;
- o **maior** valor.

## Como executar

A partir do diretório deste experimento:

```bash
python stats.py 1 2 3 4 5
```

Saída esperada:

```
Média: 3.0
Menor: 1.0
Maior: 5.0
```

## Como testar

A partir do diretório deste experimento:

```bash
python -m unittest test_stats -v
```

## Estrutura

- `stats.py` — módulo principal com a função `summarize_numbers`.
- `test_stats.py` — testes automatizados (biblioteca padrão `unittest`).

## Regras de entrada

- A entrada deve ser uma lista ou tupla de números.
- A lista não pode estar vazia.
- Elementos não numéricos (incluindo booleanos) são rejeitados.

## Escopo

Este componente é isolado e não se integra ao restante do RS4-Lab.