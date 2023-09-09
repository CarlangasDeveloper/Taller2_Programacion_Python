# Lisita para guardar los numeros
lista_numeros = []
# Contador numeros positivos
posi_numeros = 0
# Contador numeros negativos
nega_numeros = 0

# While-True se ejecuta hasta el break
while True:
    numero = int(input("Ingrese un numero: "))
    # Se termina cuando ingresa 0
    if numero == 0:
        break
    # Agregar numeros a la lista inicial
    lista_numeros.append(numero)

# Se recorre cada numero de la lista 
for numero in lista_numeros:
    # Se valida si cada numero es menor que 0
    if numero < 0:
        # Los numeros negativos se suman al contador negativo
        nega_numeros += 1
    else:
        # Los numeros positivos se suman al contador positivo
        posi_numeros += 1
# Se multiplica la cantidad de numeros positivos por asterico
posi_asteriscos = "*" * posi_numeros
# Se multiplica la cantidad de numeros negativos por asterisco
nega_asteriscos = "*" * nega_numeros
print("Positivos: "+posi_asteriscos)
print("Negativos: "+nega_asteriscos)
        
    