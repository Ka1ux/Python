class musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def buscar_titulo(self, seq, x):
        for i in range(len(seq)):
            if seq[i].titulo == x:
                return i
        return -1
    
def iremos_buscar(self):
    playlist = [ musica("Bohemian Rhapsody", "Queen", "Freddie Mercury", 1975), 
                ("Imagine", "John Lennon", "John Lennon", 1971), 
                musica("Stairway to Heaven", "Led Zeppelin", "Jimmy Page, Robert Plant", 1971)
    ]

    onde_achou = self.buscar_titulo(playlist, "Imagine")
    if onde_achou == -1:
        print("Música não encontrada na playlist")
    else:
        preferida = playlist[onde_achou]
        print(f"Música encontrada: {preferida.titulo} por {preferida.interprete}, composta por {preferida.compositor} em {preferida.ano}")
        