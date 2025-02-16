# Ejemplo 6: Simulación de do-while para solicitar un número positivo
while True:
    numero = int(input("Ingrese un número positivo: "))
    if numero > 0:
        print(f"Número válido: {numero}")
        break
    else:
        print("Número inválido, intente de nuevo.")
