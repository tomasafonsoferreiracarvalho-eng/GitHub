print('Tempo inicial')
h1 = int(input('Horas\t : '))
m1 = int(input('Minutos\t : '))
s1 = int(input('Segundos\t : '))
print('Tempo final')
h2 = int(input('Horas\t : '))
m2 = int(input('Minutos\t : '))
s2 = int(input('Segundos\t : '))
ti = h1 * 3600 + m1 * 60 + s1
tf = h2 * 3600 + m2 * 60 + s2
duracao = tf - ti
h3 = duracao // 3600
m3 = (duracao % 3600 )// 60
s3 = duracao % 60
print('A corrida durou {} horas, {} minutos e {} segundos.'.format(h3, m3, s3))
