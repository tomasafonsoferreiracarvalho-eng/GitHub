num = int(input('Número : ')) #petição do número
if num<=1:                      #se o num for igual a 1 dar composto e continuar 
    print('Número Composto')
else:
    primo = True            
    for i in range(2, int(num**1/2)+1):
        if num%i == 0:
            primo = False
            break
    if primo:
        print('Número Primo')
    else:
        print('Número Composto')