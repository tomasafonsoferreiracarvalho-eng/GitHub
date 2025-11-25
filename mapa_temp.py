import random
import math
#gerar a matriz
def generateTemp():
    m = []
    for linhas in range(10):
        linhas = []
        for x in range(4):
            linhas.append( random.random()*25 + 10)
        m.append(linhas)

    return m

def printMat(m):
    for line in m:
        for e in line:
            print(e, end = "\t")
        print()

def minMAx(m):
    tmin = math.inf
    tmax = -math.inf
    for line in m:
        tmin = min(tmin , min(line))
        tmax = max(tmax , max(line))
    return tmin,tmax
def tempMedia(m):
    soma = 0 
    for line in m:
        soma += sum(line)
    return soma/40

def localizaValor(m, v):
    for y in range(10):
        for x in range(4):
            if m[y][x] == v:
                return y,x   

def quente_frio(m):
    media = tempMedia(m)
    #matriz vazia
    qf = []
    for y in range(10):
        v = []
        for x in range(4):
            if m[y][x] < media:
                v.append('Frio')
            else:
                v.append('Quente')
        qf.append(v)
    return qf

temp = generateTemp()
temp = [[random.random()*25 +10 for x in range(4) ] for y in range(10)]
printMat(temp)

m1,m2 = minMAx(temp)
print('Minimo = {} Máximo = {}'.format(m1 , m2))

print('Localização Minimo =', localizaValor(temp, m1))
print('Localização Máxima =', localizaValor(temp, m2))

print('Temperatura Media', tempMedia(temp))

norte = (sum(temp[0]) + sum(temp[1]) + sum(temp[2]))/12
print('Media norte =', norte)

printMat(quente_frio(temp))
