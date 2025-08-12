from tateti import Tateti


def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("\nTablero:")
        print(juego.mostrar_tablero())
        print(f"Turno de: {juego.jugador_actual()}")
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            resultado = juego.ocupar_una_de_las_casillas(fil, col)
            if resultado:
                print(juego.mostrar_tablero())
                print(resultado)
                break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
