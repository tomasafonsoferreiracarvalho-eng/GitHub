num = int(input('Número\t : '))
soma = 0 
divisores = []
for i in range(1 , num , 1):
    if num%i==0:
        divisores.append(i)
        soma = soma + i
print('Dvisores =', *divisores)
print('Soma =', soma) 
if soma==num:
    print('Número perfeito')
else:
    print('Número comum')
