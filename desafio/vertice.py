# qtd_vertices = int(input("Informe a quantidade de pessoas:"))

# nomes = []

# for i in range(qtd_vertices):
#     nome = input("Informe o nome da {}ª pessoa: ".format(i+1))
#     nomes.append(nome)

# # cria matriz quadrada
# matriz = [[0] * qtd_vertices for i in range(qtd_vertices)]

# for i in range(qtd_vertices):
#     for j in range(qtd_vertices):
#         # para nao perguntar se X está relacionado com X
#         if i != j: 
#             resposta = input("{0} está relacionado com {1}? [S/n] ".format(nomes[i], nomes[j]))
#             if resposta is "S" or resposta is "s":
                
class Vertice:
    anterior = None 
    
    def __init__(self, nome):
        self.__nome = nome
        self.anterior = None
