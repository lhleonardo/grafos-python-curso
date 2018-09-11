class Lista:
    inicio = None
    fim = None
    
    def adicionaVertice(self, nome, relacao):
        if(self.inicio == None):
            self.inicio = Noh(nome, relacao)
            self.fim = self.inicio
            return

        novo = Noh(nome, relacao)
        self.fim.proximo = novo
        self.fim = novo
    
    def __str__(self):
        noh = self.inicio
        saida = ""
        if(noh == None):
            return ""
        while(noh != self.fim):
            saida += str(noh.nome) + "(" + str(noh.relacao) + ")" + " -> "
            noh = noh.proximo
        saida += str(self.fim.nome) + "(" + str(self.fim.relacao) + ")"
        return saida

    def __contains__(self, nome):
        noh = self.inicio
        while(noh != None):
            if(noh.nome == nome):
                return True
            noh = noh.proximo
        return False

class Noh:
    nome = None
    proximo = None
    relacao = None
    def __init__(self, nome, relacao):
        self.nome = nome
        self.relacao = relacao