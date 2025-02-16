# Ejemplo 4: Uso de while para sumar números hasta que el usuario ingrese 0
suma = 0
num = float(input("Ingrese un número (0 para salir): "))
while num != 0:
    suma += num
    num = float(input("Ingrese un número (0 para salir): "))
print(f"La suma total es {suma}")
