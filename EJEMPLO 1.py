class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 30)

# Llamar a la función saludar
print(persona1.saludar())

