from Estruturas.MatrizAdjacencia import MatrizAdjacencia
from Estruturas.ListaAdjacencia import ListaAdjacencia
from Busca import BuscaProfundidade

def main():
    matriz = MatrizAdjacencia()
    matriz.adicionaVertice("thuza")
    matriz.adicionaVertice("ribo")
    matriz.adicionaVertice("humil")
    matriz.adicionaAresta("thuza", "ribo", "parser")
    matriz.adicionaAresta("thuza", "humil", "parser2")
    matriz.adicionaAresta("ribo", "humil", "topparser")

    print(matriz)

    lista = ListaAdjacencia()
    lista.adicionaVertice("thuza")
    lista.adicionaVertice("ribo")
    lista.adicionaVertice("humil")
    lista.adicionaAresta("thuza", "ribo", "parser")
    lista.adicionaAresta("thuza", "humil", "parser2")
    lista.adicionaAresta("ribo", "humil", "topparser")

    print(lista)

    BuscaProfundidade.buscaProfundidade(lista)

main()