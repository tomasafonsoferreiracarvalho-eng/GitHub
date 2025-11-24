h = int(input('Horas\t : '))
m = int(input('Minutos\t : '))
s = int(input('Segundos : '))
ts = h*3600 + m*60 + s
print('Passaram {} depois da meia-noite.'.format(ts))