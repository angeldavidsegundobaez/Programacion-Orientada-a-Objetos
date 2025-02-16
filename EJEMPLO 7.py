class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def mostrar_info(self):
        return f"La película '{self.titulo}' fue dirigida por {self.director}."

pelicula1 = Pelicula("Inception", "Christopher Nolan")
print(pelicula1.mostrar_info())
