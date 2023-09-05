# Importamos la biblioteca "random" para generar números aleatorios.
import random

# Generamos un número aleatorio entre 0 y 100 y lo almacenamos en la variable "aletoria".
aletoria = random.randint(0, 100)

# Inicializamos una variable "intentos" en 0 para llevar un registro de los intentos del usuario.
intentos = 0

# Creamos un bucle que se ejecutará indefinidamente hasta que el usuario adivine el número.
while True:
    # Solicitamos al usuario que ingrese el número que crea correcto.
    numero_usuario = int(input("\nADIVINA EL NÚMERO (0 a 100): "))

    # Comparamos el número ingresado por el usuario con el número aleatorio generado.
    if numero_usuario < aletoria:
        # Si el número ingresado por el usuario es menor, mostramos un mensaje y aumentamos el contador de intentos.
        intentos += 1
        print(f"El número aleatorio es mayor que {numero_usuario}\nIntento #{intentos}")

    elif numero_usuario > aletoria:
        # Si el número ingresado por el usuario es mayor, mostramos un mensaje y aumentamos el contador de intentos.
        intentos += 1
        print(f"El número aleatorio es menor que {numero_usuario}\nIntento #{intentos}")

    else:
        # Si el usuario adivina el número, mostramos un mensaje y el número de intentos.
        intentos += 1
        print(f"LO HALLASTE \nEl número es {numero_usuario}\nAdivinaste en {intentos} intentos")

        # Salimos del bucle usando 'break'.
        break