class Restaurante:
    def __init__(self, nombre, tipo_comida):
        self.nombre = nombre
        self.tipo_comida = tipo_comida

    def info(self):
        return f"El restaurante {self.nombre} sirve comida {self.tipo_comida}."

restaurante1 = Restaurante("El Buen Sabor", "Mexicana")
print(restaurante1.info())
