# If
numeroIf = int(input("Introduce un número: "))
if numeroIf > 0:
    print("El número es positivo")
elif numeroIf < 0:
    print("El número es negativo")
else:
    print("El número es 0")

# While
numeroWhile = 0
while numeroWhile < 3:
    numeroWhile += 1
    print("El valor de la variable numeroWhile es:", numeroWhile)

# Do While
numeroDoWhile = 0
while True:
    numeroDoWhile += 1
    print("El valor de la variable numeroDoWhile es:", numeroDoWhile)
    if numeroDoWhile >= 1:
        break

# For
for numeroFor in range(4):
    print("El valor de la variable numeroFor es:", numeroFor)

# Switch
estacion = input("Introduce una estación del año: ")
switch = {
    "primavera": "Estamos en primavera",
    "verano": "Estamos en verano",
    "otoño": "Estamos en otoño",
    "invierno": "Estamos en invierno"
}
print(switch.get(estacion.lower(), "No es una estación del año"))