def magic_square(matrix):
    #valor das somas
    s = sum(matrix[0])
    #verificar as linhas
    for line in matrix:
        if sum(line) != s:
            return False
    #verificar as colunas
    for x in range(len(matrix[0])):
        soma_coluna = 0
        for y in range(len(matrix)):
            soma_coluna += matrix[y][x]
        if soma_coluna != s:
            return False
    #verificar diagonal principal
    soma_diagonal = 0
    for i in range(len(matrix)):
        soma_diagonal += matrix[i][i]
    if soma_diagonal != s:
        return False
    #verificar diagonal inversa
    soma_diagonal = 0
    for i in range(len(matrix)):
        soma_diagonal += matrix[i][len(matrix)-i-1]
    if soma_diagonal != s:
        return False
    #e um quadrado magico
    return True
matrix = [
            [8,0,7],
            [4,5,6],
            [3,10,2],
        ]
print(magic_square(matrix))