tiempo_total = 0

while True:
    tiempo_tramo = int(input("Ingrese la duración del tramo en minutos (0 para finalizar): "))

    if tiempo_tramo == 0:
        break  # Salir del bucle si se ingresa 0
    tiempo_total += tiempo_tramo

# Calcular las horas y minutos totales
horas = tiempo_total // 60
minutos = tiempo_total % 60

print(f"El tiempo total de viaje es: {horas} horas {minutos} minutos")