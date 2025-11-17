print('Divisores de um número')
num = int(input('Número : '))
print('Divisores :', end=' ')
for i in range(1, num+1,1):
    if num%i==0:
        print(i, end = (' '))