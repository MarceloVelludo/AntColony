import numpy as np
from random import randint
from random import seed
from Mapa import Mapa

class Formiga:

    def __init__(self, e):
        seed(1)
        self.cidadesNVisitadas = np.array((range(0, e)))
        self.rota = np.array()
        self.tamanhoRota = 0
        self.cidadeAtual = randint(0, e)

    #Remove a cidade visitada da lista de cidades N visitadas.
    def removeCidadeVisitada(self, cidade):
        self.cidadesNVisitadas.remove(cidade)
        return
    #Adiciona a nova cidade a roda e faz as atualizações necessarias no posicionamento da formiga.
    def adicionaRota(self, cidade, mapa):
        self.rota = np.append(cidade)
        self.removeCidade(cidade)
        self.cidadeAtual = cidade
        self.tamanhoRota = Mapa.calculaTamanhoRota(mapa, rota=self.rota)
        return
