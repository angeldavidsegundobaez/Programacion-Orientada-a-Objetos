class Computadora:
    def __init__(self, marca, procesador):
        self.marca = marca
        self.procesador = procesador

    def especificaciones(self):
        return f"Computadora {self.marca} con procesador {self.procesador}."

pc1 = Computadora("Dell", "Intel i7")
print(pc1.especificaciones())
