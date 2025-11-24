import math 


print('Teorema de Pitágoras')
ca = float(input('Cateto A\t : '))
cb = float(input('Cateto B\t : '))
hip = math.sqrt(ca**2 + cb**2)
print('Hipotenusa\t : {}'.format(hip))
