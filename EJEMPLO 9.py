class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalles(self):
        return f"Este es un {self.marca} modelo {self.modelo}."

celular1 = Celular("Samsung", "Galaxy S21")
print(celular1.detalles())
