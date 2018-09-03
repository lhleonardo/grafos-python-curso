class MatrizAdjacencia:
    _matriz = None

    def __init__(self):
        self._matriz = {}

    def adicionaVertice(self, nome):
        if(nome in self._matriz):
            return "Item já inserido"

        self._matriz[nome] = {}
        for chave in self._matriz:
            self._matriz[nome][chave] = ""
            self._matriz[chave][nome] = ""

    def adicionaAresta(self, nomeV1, nomeV2, relacao):
        self._matriz[nomeV1][nomeV2] = relacao
        self._matriz[nomeV2][nomeV1] = relacao


    def escreveMatriz(self):
        saida = "\t"
        for linha in self._matriz:
            saida += str(linha) + "\t"
        saida += "\n"
        for coluna in self._matriz:
            saida += str(coluna)
            for linha in self._matriz:
                saida += ("\t" + str(self._matriz[linha][coluna]))
            saida += "\n"
        print(saida)


