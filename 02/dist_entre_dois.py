import math

print('Distância entre dois pontos')
print('1º Ponto')
x1 = float(input('Coordenada X\t : '))
y1 = float(input('Coordenada Y\t : '))
print('2º Ponto')
x2 = float(input('Coordenada X\t : '))
y2 = float(input('Coordenada Y\t : '))
dist = math.sqrt((y2-y1)**2 + (x2-x1)**2)
print('\nDistância\t: {}'.format(dist))