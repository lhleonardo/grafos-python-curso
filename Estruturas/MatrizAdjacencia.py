class MatrizAdjacencia:
    matriz = None

    def __init__(self):
        self.matriz = {}

    def adicionaVertice(self, nome):
        if(nome in self.matriz):
            return "Item já inserido"

        self.matriz[nome] = {}
        for chave in self.matriz:
            self.matriz[nome][chave] = ""
            self.matriz[chave][nome] = ""

    def adicionaAresta(self, nomeV1, nomeV2, relacao):
        if(self.matriz[nomeV1][nomeV2] != ""):
            return "Ja ha uma relacao entre os vertices"
        self.matriz[nomeV1][nomeV2] = relacao
        self.matriz[nomeV2][nomeV1] = relacao


    def __str__(self):
        saida = "\t"
        for linha in self.matriz:
            saida += str(linha) + "\t"
        saida += "\n"
        for coluna in self.matriz:
            saida += str(coluna)
            for linha in self.matriz:
                saida += ("\t" + str(self.matriz[linha][coluna]))
            saida += "\n"
        return saida


