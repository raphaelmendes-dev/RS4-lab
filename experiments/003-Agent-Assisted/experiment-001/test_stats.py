"""Testes automatizados para o módulo stats do Experiment-001.

Usa apenas a biblioteca padrão do Python (unittest).
"""

import unittest

from stats import summarize_numbers


class TestSummarizeNumbers(unittest.TestCase):
    """Testes para a função summarize_numbers."""

    def test_media_menor_maior_basico(self):
        """Deve calcular média, menor e maior de uma lista simples."""
        result = summarize_numbers([1, 2, 3, 4, 5])
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 5)

    def test_lista_com_um_elemento(self):
        """Com um único elemento, média, menor e maior são iguais."""
        result = summarize_numbers([7])
        self.assertEqual(result["mean"], 7.0)
        self.assertEqual(result["min"], 7)
        self.assertEqual(result["max"], 7)

    def test_numeros_negativos(self):
        """Deve lidar corretamente com números negativos."""
        result = summarize_numbers([-5, -1, -10])
        self.assertEqual(result["mean"], -16 / 3)
        self.assertEqual(result["min"], -10)
        self.assertEqual(result["max"], -1)

    def test_numeros_decimais(self):
        """Deve lidar corretamente com números decimais."""
        result = summarize_numbers([1.5, 2.5, 3.0])
        self.assertEqual(result["mean"], 7.0 / 3)
        self.assertEqual(result["min"], 1.5)
        self.assertEqual(result["max"], 3.0)

    def test_tupla_como_entrada(self):
        """Deve aceitar tuplas como entrada."""
        result = summarize_numbers((4, 8, 12))
        self.assertEqual(result["mean"], 8.0)
        self.assertEqual(result["min"], 4)
        self.assertEqual(result["max"], 12)

    def test_lista_vazia_levanta_valueerror(self):
        """Lista vazia deve levantar ValueError."""
        with self.assertRaises(ValueError):
            summarize_numbers([])

    def test_entrada_nao_lista_levanta_typeerror(self):
        """Entrada que não é lista/tupla deve levantar TypeError."""
        with self.assertRaises(TypeError):
            summarize_numbers("1,2,3")

    def test_elemento_nao_numerico_levanta_typeerror(self):
        """Elemento não numérico deve levantar TypeError."""
        with self.assertRaises(TypeError):
            summarize_numbers([1, 2, "a"])

    def test_booleanos_sao_rejeitados(self):
        """Booleanos não devem ser tratados como números."""
        with self.assertRaises(TypeError):
            summarize_numbers([1, True, 3])


if __name__ == "__main__":
    unittest.main()