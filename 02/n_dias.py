def proximo_dia(d,m,a):
  if m==12 and d==31 :
    return 1,1,a+1
  if d == num_dias(m,a):
    return 1,m+1,a
  return d+1,m,a
ano = int(input('Ano\t : '))
mes = int(input('Mês\t : '))
dia = int(input('Dia\t : '))
dia,mes,ano = proximo_dia(dia,mes,ano)
print('dia seguinte',dia,'/',mes,'/',ano)