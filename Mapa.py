import random
import bisect
import numpy as np

class Mapa:
    pesos = 0
    e = 0
    visibilidade = 0
    feromonios = 0
    distancia = 0
    alpha = 0
    beta = 0
    localizacoes = 0
    rho = 0
    q = 0


    def __init__(self, e, tal, localizacoes, alpha, beta, rho, q):
        self.feromonios = np.full((e, e), tal)
        self.distancia = self.calculaDistancia(localizacoes)
        self.e = e
        self.visibilidade = self.calculaVisibilidade()
        self.alpha = alpha
        self.beta = beta
        self.localizacoes = localizacoes
        self.rho = rho
        self.q = q

    #função utilizada no random.
    def cdf(pesos):
        total = sum(pesos)
        result = []
        cumsum = 0
        for w in pesos:
            cumsum += w
            result.append(cumsum / total)
        return result

    ##Escolhe a próxima cidade que a formiga ira
    def escolhe(self, cidades, pesos):
        assert len(cidades) == len(pesos)
        cdf_vals = self.cdf(pesos)
        x = random.random()
        idx = bisect.bisect(cdf_vals, x)
        return cidades[idx]

    ##Calcula o somatorio da multiplicação entre a visibilidade e
    ##do peso dos feromonios para auxiliar no calculo da probabilidade.
    def somatorioFeromoniosN(self, cidadesNVisitadas, cidadeAtual):
        somatorio = 0
        for i2 in cidadesNVisitadas:
            somatorio += ((self.feromonios[cidadeAtual][i2])**self.alpha)*((self.visibilidade[cidadeAtual][i2])**self.beta)
        return somatorio

   #Calcula os pesos por formiga
    def calculaProbabilidades(self, cidadesNVisitadas, cidadeAtual):
        probabilidades = np.zeros(self.e)
        somatorio = self.somatorioFeromoniosN(cidadesNVisitadas)
        for i2 in cidadesNVisitadas:
                probabilidades[i2] = (((self.feromonios[cidadeAtual][i2])**self.alpha)*((self.visibilidade[cidadeAtual][i2])**self.beta))/(somatorio)
        return probabilidades

    #Atualiza o Mapa de feromonio de acordo com o local onde a formiga passou.
    def insereFeromonio(self):
        return

    #Calcula a visibilidade para auxiliar no calculo da probabilidade.
    def calculaVisibilidade(self):
        self.visibilidade = np.zeros((self.e, self.e))
        for i1 in enumerate(range(self.e)):
            for i2 in enumerate(range(self.e)):
                self.visibilidade[i1][i2] = 1/self.distancia[i1][i2]

        return self.visibilidade

    #Calcula as Distancias entre cidades.
    def calculaDistancia(self, localizacoes):
        for i1 in enumerate(range(self.e)):
            for i2 in enumerate(range(self.e)):
                self.distancias[i1][i2] = ((localizacoes[i1][0] - localizacoes[i2][0])**2 + (localizacoes[i1][1] - localizacoes[i2][1])**2)**(1/2)

        return self.distancias

    #Calcula o tamanho da Rota.
    def calculaTamanhoRota(self, rota):
        tamanho = 0
        cidadeAtual = rota[0]
        for i2 in rota:
            if cidadeAtual == i2:
                continue
            tamanho += self.distancia[cidadeAtual][i2]

        return tamanho

    def calculaDeltaFeromonio(self, l):
        return self.q / l

        #atualiza a trila de feromonios.
    def atualizaFeromonios(self, rota):
        self.feromonios[rota[-1]][rota[-2]] = (1-self.rho)*self.feromonios[rota[-1]][rota[-2]] + self.calculaDeltaFeromonio(self.calculaDistancia([rota[-1], rota[-2]]))
        return


