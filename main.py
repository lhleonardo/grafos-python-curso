from Estruturas.MatrizAdjacencia import MatrizAdjacencia

def main():
    matriz = MatrizAdjacencia()
    matriz.adicionaVertice("thuza")
    matriz.adicionaVertice("ribo")
    matriz.adicionaVertice("humil")
    matriz.adicionaAresta("thuza", "ribo", "parser")
    matriz.adicionaAresta("thuza", "humil", "parser2")
    matriz.adicionaAresta("ribo", "humil", "topparser")

    matriz.escreveMatriz()

main()