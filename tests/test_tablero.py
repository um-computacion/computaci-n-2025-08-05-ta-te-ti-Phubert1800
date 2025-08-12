import unittest
from src.tablero import Tablero


class TestTablero(unittest.TestCase):
    def test_tablero_inicializa_vacio(self):
        t = Tablero()
        for fila in t.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, " ")

    def test_poner_la_ficha(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.contenedor[0][0], "X")

    def test_no_se_puede_poner_en_casilla_ocupada(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        with self.assertRaises(ValueError):
            t.poner_la_ficha(0, 0, "0")

    def test_ganador_fila(self):
        t = Tablero()
        for col in range(3):
            t.poner_la_ficha(1, col, "X")
        self.assertEqual(t.hay_ganador(), "X")

    def test_ganador_columna(self):
        t = Tablero()
        for fil in range(3):
            t.poner_la_ficha(fil, 2, "0")
        self.assertEqual(t.hay_ganador(), "0")

    def test_ganador_diagonal_principal(self):
        t = Tablero()
        for i in range(3):
            t.poner_la_ficha(i, i, "X")
        self.assertEqual(t.hay_ganador(), "X")

    def test_ganador_diagonal_secundaria(self):
        t = Tablero()
        t.poner_la_ficha(0, 2, "0")
        t.poner_la_ficha(1, 1, "0")
        t.poner_la_ficha(2, 0, "0")
        self.assertEqual(t.hay_ganador(), "0")


if __name__ == "__main__":
    unittest.main()
