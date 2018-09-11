from Estruturas.Lista import Lista

class ListaAdjacencia:
    listaAdj = None
    
    def __init__(self):
        self.listaAdj = {}
    
    def adicionaVertice(self, nome):
        if(nome in self.listaAdj):
            return "Item ja inserido"
        
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
