from Estruturas.Lista import Lista
from Estruturas.Vertice import Vertice

class ListaAdjacencia:
    listaAdj = None
    vertices = None

    def __init__(self):
        self.listaAdj = {}
        self.vertices = {}
    
    def adicionaVertice(self, nome):
        if(nome in self.vertices):
            return "Item ja inserido"
        
        v = Vertice(nome)
        self.vertices[nome] = v
        self.listaAdj[nome] = Lista()

    def adicionaAresta(self, nomeV1, nomeV2, relacao):
        if(nomeV2 in self.listaAdj[nomeV1]):
            return "Ja ha uma relacao entre os vertices"
        
        self.listaAdj[nomeV1].adicionaVertice(nomeV2, relacao)
        self.listaAdj[nomeV2].adicionaVertice(nomeV1, relacao)

    def __str__(self):
        saida = ""
        
        for elemento in self.listaAdj:
            saida += str(elemento) + ": " + str(self.listaAdj[elemento]) + "\n"
        
        return saida

    def saoVizinhos(self, v1, v2):
        if(v1 not in self.listaAdj):
            return False
        if(v2 not in self.listaAdj):
            return False
        if(v2 not in self.listaAdj[v1]):
            return False
        return True

    def getVizinhos(self, v):
        vizinhos = []
        listaVizinhos = self.listaAdj[v]
        viz = listaVizinhos.inicio
        while(viz != None):
            vizinhos.append(viz.nome)
            viz = viz.proximo
        return vizinhos

    def retornaRelacao(self, v1, v2):
        vizinho = self.listaAdj[v1].inicio
        while(vizinho != None and vizinho.nome != v2):
            vizinho = vizinho.proximo
        if(vizinho == None):
            return ""
        return vizinho.relacao