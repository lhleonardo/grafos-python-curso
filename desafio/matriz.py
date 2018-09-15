from vertice import Vertice

class MatrizAdjacencia:

    matriz = None
    vertices = None

    def __init__(self):
        self.matriz = {}
        self.vertices = {}

    def adicionaVertice(self, nome):
        if (nome in self.vertices):
            return "Item já foi inserido"

        self.vertices[nome] = Vertice(nome)
        self.matriz[nome] = {}

        for chave in self.matriz:
            self.matriz[chave][nome] = 0
            self.matriz[nome][chave] = 0
    def adicionaRelacao(self, vertice1, vertice2, relacao):
        if (vertice1 not in self.matriz or vertice2 in not self.matriz):
            return "Um dos vertices nao existem"
        
        if (self.matriz[vertice1][vertice2] )

        self.matriz[vertice1][vertice2] = relacao
    def __str__(self):
        saida = "\t"

        for linha in self.matriz:
            saida += str(linha) + "\t"
        
        saida += "\n"

        for coluna in self.matriz:
            saida += str(coluna)
            for linha in self.matriz:
                saida += ("\t" + str(self.matriz[linha][coluna]))
            
            saida += "\n"

        return saida