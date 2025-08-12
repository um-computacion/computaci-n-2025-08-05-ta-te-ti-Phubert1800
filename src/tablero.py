class Tablero:
    def __init__(self):
        self.contenedor = [[" " for _ in range(3)] for _ in range(3)]

    def poner_la_ficha(self, fil, col, ficha):

        if fil < 0 or fil > 2 or col < 0 or col > 2:
            raise ValueError("Posición fuera de rango")
        if self.contenedor[fil][col] != " ":
            raise ValueError("La casilla ya está ocupada")
        self.contenedor[fil][col] = ficha

    def hay_ganador(self):

        for fila in self.contenedor:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        for col in range(3):
            if (
                self.contenedor[0][col] != " "
                and self.contenedor[0][col] == self.contenedor[1][col]
                and self.contenedor[1][col] == self.contenedor[2][col]
            ):
                return self.contenedor[0][col]

        if (
            self.contenedor[0][0] != " "
            and self.contenedor[0][0] == self.contenedor[1][1]
            and self.contenedor[1][1] == self.contenedor[2][2]
        ):
            return self.contenedor[0][0]
        if (
            self.contenedor[0][2] != " "
            and self.contenedor[0][2] == self.contenedor[1][1]
            and self.contenedor[1][1] == self.contenedor[2][0]
        ):
            return self.contenedor[0][2]
        return None
