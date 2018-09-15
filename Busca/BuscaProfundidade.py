class BuscaProfundidade:
    tempo = 0
    listaTopologica = []

    def buscaProfundidadeRecursivo(self, grafo, verticeAtual, anterior):
        if(anterior == None and self.tempo != 0):
            verticeAtual.anterior = anterior
        if(verticeAtual.marcado):
            return
        verticeAtual.tempoAbertura = self.tempo
        self.tempo += 1
        verticeAtual.anterior = anterior
        verticeAtual.marcado = True
        for nomeVertice in grafo.vertices:
            vertice = grafo.vertices[nomeVertice]
            if(grafo.saoVizinhos(verticeAtual.nome, nomeVertice) and not(vertice.marcado)):
                self.buscaProfundidadeRecursivo(grafo, vertice, verticeAtual)
        verticeAtual.tempoFechamento = self.tempo
        self.tempo += 1
        self.listaTopologica.append(verticeAtual)

    def buscaProfundidade(self, grafo):
        vertices = grafo.vertices
        for chave in vertices:
            vertices[chave].marcado = False
            vertices[chave].anterior = None
        for chave in vertices:
            if(not vertices[chave].marcado):
                self.buscaProfundidadeRecursivo(grafo, vertices[chave], None)

        for vertice in vertices:
            print("Anterior:", end=' ')
            if(vertices[vertice].anterior != None):
                print(vertices[vertice].anterior.nome)
            else:
                print("None")
            print('vertice:', end=' ')
            print(vertices[vertice].nome)
            print("tempoA: " + str(vertices[vertice].tempoAbertura) + " tempoF: " + str(vertices[vertice].tempoFechamento))
            print()


    