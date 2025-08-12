import unittest
from src.tateti import Tateti


class TestCLI(unittest.TestCase):
    def test_jugada_ganadora(self):
        juego = Tateti()

        self.assertIsNone(juego.ocupar_una_de_las_casillas(0, 0))

        self.assertIsNone(juego.ocupar_una_de_las_casillas(1, 0))

        self.assertIsNone(juego.ocupar_una_de_las_casillas(0, 1))

        self.assertIsNone(juego.ocupar_una_de_las_casillas(1, 1))

        resultado = juego.ocupar_una_de_las_casillas(0, 2)
        self.assertIsNotNone(resultado)
        self.assertIn("gana", resultado)

    def test_turno_alternado(self):
        juego = Tateti()
        self.assertEqual(juego.jugador_actual().ficha, "X")
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.jugador_actual().ficha, "0")


if __name__ == "__main__":
    unittest.main()
