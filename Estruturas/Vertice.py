class Vertice:
    nome = None
    marcado = None
    anterior = None

    def __init__(self, nome):
        self.marcado = False
        self.nome = nome
        self.anterior = None