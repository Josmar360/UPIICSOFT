# Josmar Gustavo Palomino Castelan
# Josmar360
# Declaracion de variable Palabra
Palabra = str(input("Dame una palabra para saber si es un palíndromo: "))

# Función para comparar la palabra
def Palindromo(cadena):
    # Convierte la cadena a minúsculas y quita los espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    # Compara la cadena original con su inversa y regresa la funcion
    return cadena == cadena[::-1]

# Codigo principal
# Resultado de comparacion usando un If
if Palindromo(Palabra):
    print(f"{Palabra} es un palíndromo")
else:
    print(f"{Palabra} no es un palíndromo")