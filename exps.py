#lista = [2,4,6,8,10,12,14,16,18,20]
#print(lista)
#print(lista[0 : 5])
#print('----------------------------')
#l = []
#for n in range(1,11):
#    l.append(2*n)
#print(l)
#print('----------------------------')
#l = []
#for n in range(1,11):
#    l += [2*n]
#print(l)
print('----------------------------')
l = [2*n for n in range(1,11)]
print(l,1)
print(l[0 : 5 : 1],2) #selecionar e imprimir os primeiros 5 elementos; l[:5]
print(l[-3 : : 1],3) #selecionar e imprimir os últimos três elementos; l[-3:]
print(l[1 : -1 : ],4) #selecionar e imprimir todos excepto o primeiro e o último; começa no 1 e acaba no -1 que é o penultimo positivo
print(l[0 : -1 : 2 ],5) #posições pares
print(l[1: :2],6) #posições impares
l.insert(0,0) #add zeros 
print(l,7) #adicinoar zeros 
l.pop(-1) #eliminar o último elemento
print(l,8) #eliminar o último elemento