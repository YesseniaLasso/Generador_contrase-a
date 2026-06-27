# ============================================
# GENERADOR DE CONTRASEÑAS
# ============================================
import random

print("*************GENERADOR DE CONTRASEÑAS****************")

longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
while longitud < 8:
    print("¡Ingrese una longitud mayor o igual a 8 y menor de 64!")
    longitud = int(input("Ingrese longitud: "))

# Tuplas con los grupos de caracteres
mayusculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

minusculas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

simbolos = ("!", "@", "#", "$", "%", "^", "&", "*")

while True:
    print("\nSeleccione los tipos de caracteres (1 = Sí, 0 = No):")
    usar_mayusculas = int(input("¿Desea utilizar Mayúsculas (A-Z)? "))
    usar_minusculas = int(input("¿Desea utilizar Minúsculas (a-z)? "))
    usar_numeros    = int(input("¿Desea utilizar Números (0-9)? "))
    usar_simbolos   = int(input("¿Desea utilizar Símbolos (!@#$)? "))

    if usar_mayusculas + usar_minusculas + usar_numeros + usar_simbolos >= 2:
        break
    print("Debe seleccionar al menos dos opciones.")

# Armar el conjunto como tupla sumando las tuplas seleccionadas
conjunto = ()
if usar_mayusculas == 1:
    conjunto = conjunto + mayusculas
if usar_minusculas == 1:
    conjunto = conjunto + minusculas
if usar_numeros == 1:
    conjunto = conjunto + numeros
if usar_simbolos == 1:
    conjunto = conjunto + simbolos
#print("La contraseña se generará a partir de este contenido:", conjunto)
# Generar la contraseña
contrasena = ""

for i in range(longitud):
    indice = random.randint(0, len(conjunto) - 1)
    contrasena = contrasena + conjunto[indice]

print("\n Tu contraseña generada es:", contrasena)
