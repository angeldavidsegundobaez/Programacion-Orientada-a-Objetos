class Animal:
    def __init__(self, especie, sonido):
        self.especie = especie
        self.sonido = sonido

    def hacer_sonido(self):
        return f"El {self.especie} hace {self.sonido}."

animal1 = Animal("Perro", "Ladrido")
print(animal1.hacer_sonido())
