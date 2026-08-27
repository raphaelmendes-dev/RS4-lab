# Experiment-004 — Local Triage Automation

## Notes

### Referência

O baseline humano utilizado neste experimento está registrado separadamente em:

`baseline.md`

A amostra utilizada nas baterias com os modelos é a mesma utilizada no baseline, permitindo comparação posterior sob o mesmo conjunto de documentos.

---

# 27/08/2026 — Primeira bateria

## Modelo

`llama3.2:3b`

Primeira bateria experimental com os seis arquivos utilizados no baseline humano.

| Arquivo                  | Tempo de leitura | Tempo total | Nota |
| ------------------------ | ---------------: | ----------: | ---: |
| etapa1.docx              |          89,05 s |    105,57 s |    2 |
| INT_ia.docx              |          54,03 s |     63,50 s |    2 |
| makedown.md              |          61,53 s |    173,48 s |    0 |
| proposta_maltbot.docx    |           7,20 s |     15,70 s |    2 |
| resultado.txt            |           9,58 s |     22,18 s |    2 |
| Como estruturar... .docx |          17,72 s |     32,60 s |    2 |

### Resultado

**Tempo total da bateria:** 413,03 s

**Tempo médio por arquivo:** 68,84 s

**Baseline humano:** 30,5 s/arquivo

Qualidade dos resumos:

* 5 arquivos receberam nota 2.
* 1 arquivo recebeu nota 0.
* Nenhum recebeu nota 3.

### Observações

* O modelo conseguiu produzir resumos considerados adequados em 5 dos 6 arquivos.
* O arquivo `makedown.md` apresentou falha significativa de aderência à instrução.
* O documento tinha aproximadamente 300 linhas e o modelo produziu um "resumo" de aproximadamente 202 linhas.
* Nesse caso, o modelo não apresentou adequadamente os pontos centrais solicitados.
* Houve grande variação no tempo total entre os arquivos.
* O modelo respondeu em português.
* O modelo não possui acesso direto aos arquivos do sistema; o conteúdo precisou ser fornecido ao modelo.
* Em teste exploratório anterior, quando solicitado a acessar `baseline.md` sem receber seu conteúdo, informou corretamente que não tinha acesso ao arquivo.
* Em teste exploratório de autoavaliação, produziu uma narrativa sobre sua própria atuação. Essa resposta não foi considerada métrica de desempenho.

### Avaliação

A primeira bateria indica que o modelo conseguiu produzir resumos úteis em parte dos casos, mas apresentou falha significativa de aderência ao formato solicitado em um dos arquivos.

Os resultados não permitem concluir que o modelo seja adequado ou inadequado para a automação de triagem.

---

# 27/08/2026 — Segunda bateria

## Modelo

`qwen2.5:3b`

Segunda bateria experimental utilizando os mesmos seis arquivos, a mesma tarefa e o mesmo protocolo utilizado na bateria anterior.

| Arquivo                  | Tempo de leitura | Tempo total | Nota |
| ------------------------ | ---------------: | ----------: | ---: |
| etapa1.docx              |          16,75 s |     20,71 s |    3 |
| INT_ia.docx              |          45,99 s |     57,81 s |    3 |
| makedown.md              |          39,46 s |    170,09 s |    1 |
| proposta_maltbot.docx    |           7,80 s |     12,90 s |    3 |
| resultado.txt            |           8,54 s |     19,56 s |    3 |
| Como estruturar... .docx |          17,86 s |     28,95 s |    3 |

### Resultado

**Tempo total da bateria:** 310,02 s

**Tempo médio por arquivo:** 51,67 s

**Baseline humano:** 30,5 s/arquivo

Qualidade dos resumos:

* 5 arquivos receberam nota 3.
* 1 arquivo recebeu nota 1.
* Nenhum recebeu nota 0 ou nota 2.

**Média de qualidade:** 2,67/3

### Observações

* O modelo apresentou respostas consideradas adequadas em 5 dos 6 arquivos.
* `etapa1.docx` recebeu nota 3.
* `INT_ia.docx` recebeu nota 3.
* `proposta_maltbot.docx` recebeu nota 3. O resumo foi considerado claro, entregou a essência do documento e utilizou 3 linhas.
* `resultado.txt` recebeu nota 3.
* `Como estruturar... .docx` recebeu nota 3.
* O arquivo `makedown.md` apresentou novamente dificuldade em produzir uma explicação simples de um documento grande.
* No `makedown.md`, o modelo não respeitou o limite de linhas definido no protocolo.
* O `makedown.md` recebeu nota 1.
* O tempo de leitura do `makedown.md` foi menor que o observado no Llama 3.2 3B, porém o tempo total permaneceu elevado.
* O modelo respondeu em português.

### Avaliação

A segunda bateria apresentou, nesta amostra, tempo médio inferior ao observado na primeira bateria com o Llama 3.2 3B e notas de qualidade superiores na avaliação humana.

Entretanto, o arquivo `makedown.md` apresentou novamente dificuldade de aderência ao formato solicitado, embora com avaliação superior à observada no Llama 3.2 3B.

Os resultados desta bateria não permitem concluir que o Qwen 2.5 3B seja superior de forma geral ao Llama 3.2 3B ou que seja adequado para automação de triagem.

Os dados deverão ser comparados formalmente utilizando o mesmo protocolo e as mesmas métricas.

---

# Observação metodológica

As duas baterias foram realizadas utilizando:

* os mesmos seis arquivos;
* a mesma tarefa;
* o mesmo protocolo;
* avaliação humana da qualidade;
* separação entre tempo de leitura e tempo total.

O objetivo desta etapa é produzir uma primeira observação comparável entre os modelos.

As medições de tempo desta fase foram realizadas manualmente.

A medição automatizada será implementada posteriormente, após o fechamento e validação das métricas do experimento.

---

# Próximos passos

1. Fechar o formato do `metrics.json`.
2. Registrar no `metrics.json` os dados do baseline, Llama 3.2 3B e Qwen 2.5 3B.
3. Conferir os cálculos e a consistência dos dados.
4. Revisar os arquivos antes do versionamento.
5. Executar `git status`.
6. Versionar e enviar as alterações ao GitHub.
7. Posteriormente, implementar a medição automática em Python.
