class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def presentarse(self):
        return f"Soy {self.nombre} y estudio {self.carrera}."

estudiante1 = Estudiante("Ana", "Ingeniería")
print(estudiante1.presentarse())
