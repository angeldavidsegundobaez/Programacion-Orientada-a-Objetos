class Ciudad:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def ubicacion(self):
        return f"La ciudad de {self.nombre} está en {self.pais}."

ciudad1 = Ciudad("Madrid", "España")
print(ciudad1.ubicacion())
