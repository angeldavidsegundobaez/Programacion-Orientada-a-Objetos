class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def reproducir(self):
        return f"Reproduciendo '{self.titulo}' de {self.artista}."

cancion1 = Cancion("Bohemian Rhapsody", "Queen")
print(cancion1.reproducir())
