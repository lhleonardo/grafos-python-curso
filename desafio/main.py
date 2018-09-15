from matriz import MatrizAdjacencia



def buscarEmProfundidade(grafo):
    vertices = grafo.vertices

    for chave in vertices:
        vertices[chave].marcado = False
        vertices[chave].anterior = None
    
    for chave in vertices:
        if not vertices[chave].marcado:
            visitaVertice()

def visitaVertice(grafo, vertice, anterior):
    if not vertice.marcado:
        vizinhos = grafo.matriz[vertice.nome]
        for vizinho in vizinhos:
            if (vizinhos[vizinho] != ""):
                
        
    

def main():
    m = MatrizAdjacencia()

    m.adicionaVertice("Leo")
    m.adicionaVertice("Gui")
    m.adicionaVertice("Gabi")
    m.adicionaVertice("Ruan")

    print(m.adicionaRelacao("Leo", "Gui", "Rel"))
    print(m.adicionaRelacao("Leo", "Gabi", "Rel"))
    print(m.adicionaRelacao("Leo", "Ruan", "Rel"))
    print(m.adicionaRelacao("Gui", "Gabi", "Rel"))

    print(m.saoVizinhos("Ruan", "Gui"))

    print(m)


main()