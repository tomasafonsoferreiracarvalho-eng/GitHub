nota5 = int(input('Número de notas de 5€\t : '))
din = 5*nota5
print('\nMoedas de 2€\t : {}'.format(int(din/2)))
print('Moedas de 1€\t : {}'.format(din%2))
