numero_palindromo = int(input("Ingrese un número: "))

# Se convierte el número ingresado a String
num_str = str(numero_palindromo)
    
# Comparamos el String con el String invertido
if num_str == num_str[::-1]:
    print("El número ingresado es palindromo")
else:
    print("El número ingresado NO es palindromo")