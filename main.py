from Estruturas.MatrizAdjacencia import MatrizAdjacencia
from Estruturas.ListaAdjacencia import ListaAdjacencia
from Busca.BuscaProfundidade import BuscaProfundidade
from Busca import BuscaLargura
from ExportaArqGraph import ArquivoGraph
def main():
    matriz = MatrizAdjacencia()

    entrada = ""
    while(entrada != "fim"):
        entrada = input()
        if(entrada != "fim"):
            matriz.adicionaVertice(entrada)

    entrada = ""
    while(entrada != "fim"):
        entrada = input().split()
        if(entrada[0] != "fim"):
            matriz.adicionaAresta(entrada[0], entrada[1], "Chefe")
        else:
            entrada = entrada[0]

    print(matriz)
    dfs = BuscaProfundidade()
    dfs.buscaProfundidade(matriz)

    lista = dfs.listaTopologica

    calculaAnteriores(lista)

    imprimeResultados(matriz)

def calculaAnteriores(lista):
    for i in range(len(lista) - 1):
        if(lista[i].anterior == None):
            j = i + 1
            while((j < len(lista)) and (lista[j].tempoAbertura != lista[i].tempoFechamento + 1)):
                j += 1
            lista[i].anterior = lista[j]

def imprimeResultados(grafo):
    vertices = grafo.vertices
    for vertice in vertices:
        if(vertices[vertice].anterior != None):
            print(str(vertice) + " (" + str(vertices[vertice].anterior.nome) + ")")
        else:
            print(str(vertice) + " (Presidente)")


main()