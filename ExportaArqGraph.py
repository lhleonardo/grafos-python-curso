class ArquivoGraph:
    nomaArq = ""
    arquivo = None

    def __init__(self, nomaArq):
        self.nomaArq = nomaArq
        self.arquivo = open(self.nomaArq + ".txt", "w")
        self.arquivo.write("graph G {\n")
    
    def addAresta(self, v1, v2, relacao):
        self.arquivo.write(v1 + " -- " + v2 + " [ label= " + relacao + " ]\n")
    
    def add(self, v1, v2):
        self.arquivo.write(v1 + " -- " + v2 +"\n")
    
    def addVertice(self, v1):
        self.arquivo.write(v1 +"\n")
    
    def addMatriz(self, grafo):
        vertices = grafo.vertices
        escritos = {}
        for elmento in vertices:
            escritos[elmento] = {}
            for elmento2 in vertices:
                escritos[elmento][elmento2] = False
        
        print(escritos)
        
        for chave in vertices:
            chavesVizinhos = grafo.getVizinhos(chave)
            for chaveVizinho in chavesVizinhos:
                if(not escritos[chave][chaveVizinho] and not escritos[chaveVizinho][chave]):
                    self.arquivo.write(str(chave) + " -- " + str(chaveVizinho))
                    self.arquivo.write(" [ label= " + str(grafo.retornaRelacao(chave, chaveVizinho)) + " ]\n")
                    escritos[chave][chaveVizinho] = True
        
        
    def close(self):
        self.arquivo.write('}')
        self.arquivo.close()
