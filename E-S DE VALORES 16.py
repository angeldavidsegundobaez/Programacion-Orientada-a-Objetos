# Ejemplo 15: Cálculo de descuento
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = precio - (precio * descuento / 100)
print(f"El precio final con descuento es {precio_final}")
