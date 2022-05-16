# Prepare a sua entrevista -- Python
# https://youtube.com/c/AutomationDataScience

# Desafio:
#     Crie uma função que retorne o
#     perímetro de um triângulo com base nas coordenadas de três
#     vértices.

#     Vídeo-Desafio: https://www.youtube.com/shorts/rutjLHBFobc

import math


def perimeter(lst):
    lst.append(lst[0])

    dist = 0
    for i in range(1, len(lst)):
        dist += math.dist(lst[i-1], lst[i])

    return round(dist, 2)


# -- Testes
rsp = perimeter([(-1, 0), (2, 4), (10, 5)])
print(rsp)

rsp = perimeter([(0, 1), (1, 0), (0, 1)])
print(rsp)
