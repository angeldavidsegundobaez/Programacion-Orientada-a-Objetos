# Ejemplo 11: Ingreso y salida de una lista de números
numeros = input("Ingrese números separados por espacio: ").split()
numeros = [int(n) for n in numeros]
print(f"Lista de números: {numeros}")
