print('------------------------')
print('Divisores de um número')
print('------------------------')
num = int(input('Número\t = '))
lista = 0 
print('Divisores : ',end=(''))
for i in range(1 , num+1 , 1):
    if num%i ==0:
        print(i , end=(' '))
print('\n------------------------')