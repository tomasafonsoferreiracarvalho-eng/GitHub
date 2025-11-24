print('Tempo inicial')
h = int(input('Horas\t : '))
m = int(input('Minutos\t : '))
s = int(input('Segundos : '))
ts = h * 3600 + m * 60 + s
print('Tempo final')
h2 = int(input('Horas\t : '))
m2 = int(input('Minutos\t : '))
s2 = int(input('Segundos : '))
tsf = h2 * 3600 + m2 * 60 + s2
maxi = max(ts, tsf)
mini = min(ts, tsf)
td = maxi - mini
print('A corrida durou {} segundos,'.format(td))
