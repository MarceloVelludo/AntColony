import numpy as np
from Formiga import Formiga
from Mapa import Mapa

def aco(max_it, alpha, beta, rho, N, e, q, tal, b, localizacoes):
    #inicializando elementos.
    mapa = Mapa(e, tal, localizacoes, alpha, beta, rho, q)
    formigas = np.full(e, Formiga())
    iteracao = 0

    while iteracao < max_it:
        ##localizando a melhor rota.
        # Para cada numero de formigas é construido uma rota aplicando o seguinte passo.
        for formiga in formigas:
            for i in enumerate(range(e-1)):
                proximaCidade = mapa.calculaProbabilidades(formiga.cidadesNVisitadas, formiga.cidadeAtual)
                formiga.adicionaRota(proximaCidade, mapa)

        # Avalia o tamanho da rota construída por cada formiga, se uma rota mais curta for encontrada a
        # melhor rota será atualizada.
        for formiga in formigas:
            if formiga.tamanhoRota < lmenor:
                lmenor = formiga.tamanhoRota
                melhor = formiga.rota
        #Atualiza os feromonios nas rotas que as formigas passaram.
        for formiga in formigas:
            mapa.atualizaFeromonios(formiga.rota)
        iteracao += iteracao

    return melhor, lmenor