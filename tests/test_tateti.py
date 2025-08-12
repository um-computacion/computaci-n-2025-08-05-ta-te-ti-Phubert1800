import unittest
from src.tateti import Tateti


class TestTateti(unittest.TestCase):
    def test_inicializa_con_tablero_vacio(self):
        juego = Tateti()
        for fila in juego.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, " ")

    def test_turno_inicial_es_X(self):
        juego = Tateti()
        self.assertEqual(juego.jugador_actual().ficha, "X")

    def test_alternancia_turnos(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.jugador_actual().ficha, "0")
        juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(juego.jugador_actual().ficha, "X")

    def test_ganador_detectado(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)  # X
        juego.ocupar_una_de_las_casillas(1, 0)  # 0
        juego.ocupar_una_de_las_casillas(0, 1)  # X
        juego.ocupar_una_de_las_casillas(1, 1)  # 0
        resultado = juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        self.assertIsNotNone(resultado)
        self.assertIn("gana", resultado)


if __name__ == "__main__":
    unittest.main()
