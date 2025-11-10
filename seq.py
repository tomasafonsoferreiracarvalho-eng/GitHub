print('Média de uma sequência terminada em zero')
num = int(input('Número\t : ')) #petição do primeiro número
i = 0 #contagem de 'num'
soma = 0 #soma de todos os 'num'
while num!=0:
    soma = soma + num
    i = i + 1 
    num = int(input('Número\t : ')) #colocação de todos os 'num'
if i > 0: 
    media = soma/i
    print('\nMédia\t = ',(media)) #media