# Josmar Gustavo Palomino Castelan
# Josmar360
# Declaracion de variables
Numero = int(input("Dame un número para calcular su factorial: "))

# Funcion para verificar si el numero que da el usuario es positivo
def Verificar_Positivo(Numero):
    if (Numero>=0):
        Resultado = Calcular_Factorial(Numero)
        return Resultado
    else:
        print("No me diste ningun valor positivo...")
        return 0

# Funcion para calcular el factorial que dio el usuario
def Calcular_Factorial(Numero):
    Factorial = 1
    for Aux in range(1, Numero + 1):
        Factorial = Factorial * Aux
    return Factorial

# Codigo principal 
Factorial = Verificar_Positivo(Numero)
# Verifica si se pudo calcular el factorial o no
if (Factorial != 0):
    print(f"El factorial de {Numero} es: ", Factorial)
else:
    print("No se pudo calcular ningun factorial por la razón de arriba....")