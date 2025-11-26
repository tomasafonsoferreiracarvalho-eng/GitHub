print('Calculadora')
print('Subtrair=0\nDividir=1\nSomar=2\nMultiplicar=3')
while True:
    func = int(input('Qual é a função desejada: '))
    if func in [0,1,2,3]:
        break
    else:
        print('ERRO VALOR NÃO SUPORTADO')
n1 = float(input('Número 1 : '))
n2 = float(input('Número 2 : '))
if func == 0:
    print(f'{n1}-{n2}={n1-n2}')
else:
    if func ==1:
        print(f'{n1}/{n2}={n1/n2}')
    else:
        if func == 2:
            print(f'{n1}+{n2}={n1+n2}')
        else:
            if func == 3:
                print(f'{n1}*{n2}={n1*n2}')