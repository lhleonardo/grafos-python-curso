from Estruturas.Vertice import Vertice

class MatrizAdjacencia:
    matriz = None
    vertices = None

    def __init__(self):
        self.matriz = {}
        self.vertices = {}

    def adicionaVertice(self, nome):
        if(nome in self.vertices):
            return "Item já inserido"

        v = Vertice(nome)
        self.vertices[nome] = v

        self.matriz[nome] = {}
        for chave in self.matriz:
            self.matriz[nome][chave] = ""
            self.matriz[chave][nome] = ""

    def adicionaAresta(self, nomeV1, nomeV2, relacao):
        if(self.matriz[nomeV1][nomeV2] != ""):
            return "Ja ha uma relacao entre os vertices"
        self.matriz[nomeV1][nomeV2] = relacao
        self.matriz[nomeV2][nomeV1] = relacao


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

    def saoVizinhos(self, v1, v2):
        if(v1 not in self.matriz):
            return False
        if(v2 not in self.matriz):
            return False
        if(self.matriz[v1][v2] == ""):
            return False
        return True

    def getVizinhos(self, v):
        vizinhos = []
        for chave in self.matriz:
            if(self.matriz[v][chave] != ""):
                vizinhos.append(chave)
        return vizinhos

    def retornaRelacao(self, v1, v2):
        return self.matriz[v1][v2]
