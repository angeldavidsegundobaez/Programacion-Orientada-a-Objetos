# Ejemplo 5: Descuento en una compra
monto = float(input("Ingrese el monto de la compra: "))
if monto > 100:
    descuento = monto * 0.1
    total = monto - descuento
    print(f"Se aplicó un descuento de {descuento}, el total a pagar es {total}.")
else:
    print(f"No se aplica descuento, el total a pagar es {monto}.")
