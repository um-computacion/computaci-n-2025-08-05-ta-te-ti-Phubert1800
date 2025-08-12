try:
    from .tablero import Tablero
    from .jugador import Jugador
except ImportError:
    from tablero import Tablero
    from jugador import Jugador


class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        self.jugadores = [Jugador("Jugador 1", "X"), Jugador("Jugador 2", "0")]
        self.turno = 0

    def ocupar_una_de_las_casillas(self, fil, col):
        jugador_actual = self.jugadores[self.turno]
        self.tablero.poner_la_ficha(fil, col, jugador_actual.ficha)
        ganador = self.tablero.hay_ganador()
        if ganador:
            return f"¡{jugador_actual.nombre} gana con '{ganador}'!"

        self.turno = 1 - self.turno
        return None

    def mostrar_tablero(self):
        filas = []
        for fila in self.tablero.contenedor:
            filas.append(" | ".join(fila))
        return "\n---------\n".join(filas)

    def jugador_actual(self):
        return self.jugadores[self.turno]
