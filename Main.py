from ACO import aco
from Bd import uploadLocalizacoes

max_it = 1000
alpha = 1
beta = 5
rho = 0.5
e = 52
n = e
q = 100
tal = 0.0000001
b = 5

localizacoes = uploadLocalizacoes("berlin52.txt")

melhor = aco(max_it, alpha, beta, rho, n, e, q, tal, b, localizacoes)