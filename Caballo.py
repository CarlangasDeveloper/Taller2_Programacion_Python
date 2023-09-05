# Solicita las coordenadas del caballo al usuario.
fila = int(input("Ingrese la fila del caballo (1-8): "))
columna = int(input("Ingrese la columna del caballo (1-8): "))

# Verifica si las coordenadas son válidas (entre 1 y 8).
if fila < 1 or fila > 8 or columna < 1 or columna > 8:
    print("Coordenadas inválidas. Deben estar entre 1 y 8.")
else:
    # Calcula y muestra las casillas a las que el caballo puede saltar.
    print(f"El caballo puede saltar de {fila}, {columna} a:")

    # Definimos los movimientos posibles del caballo en forma de L.
    movimientos = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    # Iteramos a través de los movimientos posibles usando un bucle.
    for i in range(len(movimientos)):
        movimiento = movimientos[i]
        nuevaFila = fila + movimiento[0]
        nuevaColumna = columna + movimiento[1]

        # Verifica si la nueva posición está dentro del tablero.
        if 1 <= nuevaFila <= 8 and 1 <= nuevaColumna <= 8:
            print(f"{nuevaColumna}, {nuevaFila}")