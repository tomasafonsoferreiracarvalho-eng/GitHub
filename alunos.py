n = int(input('Nº de alunos da turma: '))
lst = [ int(input('Nota['+str(p)+'] : ')) for p in range(n)]
print(lst)
print('Nota máxima = ',max(lst))
print('Nota mínima = ',min(lst))
media = sum(lst)/len(lst)
print('Media da turma = ',media)