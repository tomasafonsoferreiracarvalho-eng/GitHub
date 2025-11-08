#1 code no Git, simples mas usavel
#escrever "Hello World"
print('Hello World')
#escrever n vezes
n = int(input('Escrever quantas vezes Hello World\t : '))
for i in range(1,n+1,1):
    print('Hello World', end='\n')
    print('-----------------------')
#para dar a func lower ou upper temos de segignar uma func com 
#o texto e de seguida dar um nome a func que faça o upper ou lower e de seguida print essa última
wh = 'Hello World'
up = wh.upper()
print(up)

lo = wh.lower()
print(lo)
#para inverter é quase o mesmo só que com [::-1]
invert = wh[::-1]
print(invert)