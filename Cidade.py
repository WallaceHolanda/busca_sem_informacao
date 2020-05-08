class Cidade:
    def __init__(self, nome): #Construtor
        self.nome = nome
        self.visitado = False
        self.adjacentes = [] #Lista de Cidades Adjacentes
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)
        
'''
c = Cidade("Teste")
c.nome
c.visitado
'''