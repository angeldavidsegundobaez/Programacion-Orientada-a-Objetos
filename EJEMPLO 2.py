class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Este coche es un {self.marca} {self.modelo}."

coche1 = Coche("Toyota", "Corolla")
print(coche1.describir())
