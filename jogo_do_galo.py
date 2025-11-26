import random

jogador = ["X", "O"]

def sortear_jogador():
    return random.randint(0,1)

def imprimir_jogo(m):
    for line in m:
        for elem in line:
            print(elem, end="\t")
        print()

def iniciar_jogo():
    return [["." for _ in range(3)] for _ in range(3)]

def ler_indice(msg):
    #lê um índice de 0 a 2, repetindo até ser válido
    while True:
        try:
            valor = int(input(msg))
            if valor < 0 or valor > 2:
                print("Erro: número fora do intervalo (0 a 2). Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Erro: digite um número inteiro. Tente novamente.")

def obter_jogada_valida(m):
    #pede linha e coluna e valida se a posição está livre
    while True:
        linha = ler_indice("linha (0-2) = ")
        coluna = ler_indice("coluna (0-2) = ")
        if m[linha][coluna] != ".":
            print("Erro: posição ocupada. Escolha outra.")
            continue
        return linha, coluna

def jogar(m, j):
    print("Jogador", j)
    linha, coluna = obter_jogada_valida(m)
    m[linha][coluna] = j
    imprimir_jogo(m)

def ganhou(m, j):
    #verificar linhas
    for line in m:
        if line.count(j) == 3:
            return True
    #verificar colunas
    for x in range(3):
        if m[0][x] == j and m[1][x] == j and m[2][x] == j:
            return True
    #diagonais
    if m[0][0] == j and m[1][1] == j and m[2][2] == j:
        return True
    if m[0][2] == j and m[1][1] == j and m[2][0] == j:
        return True
    return False

def empate(m):
    for line in m:
        if "." in line:
            return False
    return True

#---Jogo principal---
galo = iniciar_jogo()
index = sortear_jogador()

while True:
    jogar(galo, jogador[index])
    if ganhou(galo, jogador[index]):
        print("Jogador", jogador[index], "venceu!")
        break
    if empate(galo):
        print("Empate!")
        break
    index = (index+1) % 2