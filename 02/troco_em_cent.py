troco = int(input('Troco em cêntimos\t : '))
print('Moedas de 50 cêntimos\t : {}'.format(troco // 50))
troco = troco % 50
print('Moedas de 20 cêntimos\t : {}'.format(troco // 20))
troco = troco % 20
print('Moedas de 10 cêntimos\t : {}'.format(troco // 10))
troco = troco % 10
print('Moedas de 5 cêntimos\t : {}'.format(troco // 5))
troco = troco % 5
print('Moedas de 2 cêntimos\t : {}'.format(troco // 2))
troco = troco % 2
print('Moedas de 1 cêntimo\t : {}'.format(troco // 1))


