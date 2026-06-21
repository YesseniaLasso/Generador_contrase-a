# ============================================
# GENERADOR DE CONTRASEÑAS
# ============================================

print("*************GENERADOR DE CONTRASEÑAS****************")

longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))

while longitud < 8:
    print("¡Ingrese una longitud mayor o igual a 8!")
    longitud = int(input("Ingrese longitud: "))

while True:
    print("\nSeleccione los tipos de caracteres (1 = Sí, 0 = No):")
    usar_mayusculas = int(input("¿Desea utilizar Mayúsculas (A-Z)? "))
    usar_minusculas = int(input("¿Desea utilizar Minúsculas (a-z)? "))
    usar_numeros    = int(input("¿Desea utilizar Números (0-9)? "))
    usar_simbolos   = int(input("¿Desea utilizar Símbolos (!@#$)? "))

    if usar_mayusculas + usar_minusculas + usar_numeros + usar_simbolos >= 2:
        break
    print("Debe seleccionar al menos dos opciones.")

conjunto = ""

if usar_mayusculas == 1:
    conjunto = conjunto + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if usar_minusculas == 1:
    conjunto = conjunto + "abcdefghijklmnopqrstuvwxyz"

if usar_numeros == 1:
    conjunto = conjunto + "0123456789"

if usar_simbolos == 1:
    conjunto = conjunto + "!@#$%^&*"

print("La contraseña se generará a partir de este contenido:",conjunto)

