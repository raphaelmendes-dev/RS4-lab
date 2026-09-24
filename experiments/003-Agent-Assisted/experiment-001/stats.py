"""Módulo de estatísticas para o Experiment-001.

Recebe uma lista de números e retorna a média, o menor e o maior valor.
"""


def summarize_numbers(numbers):
    """Calcula média, menor e maior valor de uma lista de números.

    Args:
        numbers: lista de números (int ou float).

    Returns:
        dict com as chaves 'mean', 'min' e 'max'.

    Raises:
        TypeError: se a entrada não for uma lista/tupla ou contiver
            elementos não numéricos.
        ValueError: se a lista estiver vazia.
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("A entrada deve ser uma lista ou tupla de números.")

    if len(numbers) == 0:
        raise ValueError("A lista não pode estar vazia.")

    for value in numbers:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(
                f"Todos os elementos devem ser números. Encontrado: {value!r}"
            )

    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


def main():
    """Interface de linha de comando simples para demonstração."""
    import sys

    try:
        raw = sys.argv[1:]
        if not raw:
            raise ValueError("Nenhum número informado. Ex.: python stats.py 1 2 3")

        numbers = [float(item) for item in raw]
        result = summarize_numbers(numbers)
        print(f"Média: {result['mean']}")
        print(f"Menor: {result['min']}")
        print(f"Maior: {result['max']}")
    except (TypeError, ValueError) as error:
        print(f"Erro: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()