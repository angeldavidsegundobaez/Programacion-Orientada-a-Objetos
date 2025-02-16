class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_info(self):
        return f"El libro '{self.titulo}' fue escrito por {self.autor}."

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
print(libro1.obtener_info())
