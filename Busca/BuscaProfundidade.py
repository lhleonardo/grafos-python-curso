def buscaProfundidade(grafo):
    vertices = grafo.vertices
    for chave in vertices:
        vertices[chave].marcado = False
        vertices[chave].anterior = None
    for chave in vertices:
        if(not vertices[chave].marcado):
            buscaProfundidadeRecursivo(grafo, vertices[chave], None)

    for vertice in vertices:
        print("Anterior:")
        if(vertices[vertice].anterior != None):
            print(vertices[vertice].anterior.nome)
        print('vertice:')
        print(vertices[vertice].nome)
        print()


def buscaProfundidadeRecursivo(grafo, verticeAtual, anterior):
    verticeAtual.anterior = anterior
    verticeAtual.marcado = True
    for nomeVertice in grafo.vertices:
        vertice = grafo.vertices[nomeVertice]
        if(grafo.saoVizinhos(verticeAtual.nome, nomeVertice) and not(vertice.marcado)):
            buscaProfundidadeRecursivo(grafo, vertice, verticeAtual)