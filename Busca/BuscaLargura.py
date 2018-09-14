def buscaLargura(grafo):
    vertices = grafo.vertices

    for chave in vertices:
        vertices[chave].marcado = False
        vertices[chave].anterior = None

    c = list(vertices.keys())[0]
    
    vertices[c].marcado = True
    
    fila = [c]
    print("inicial = " + str(c))
    while(len(fila) > 0):
        atual = fila.pop(0)
        vizinhos = grafo.getVizinhos(atual)
        for elemento in vizinhos:
            if(not vertices[elemento].marcado):
                vertices[elemento].marcado = True
                vertices[elemento].anterior = atual
                fila.append(elemento)
    
    print("resultado: ")
    for elemento in vertices:
        print(str(vertices[elemento].nome) + " " + str(vertices[elemento].anterior))



