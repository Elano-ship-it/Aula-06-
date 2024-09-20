alunos = {'Maria':99,'Cloves':88,'Ana':77,'Dio':66}
alunos['Cloves'] = 55 # Modificação da Matricula
print(alunos)
alunos.pop('Cloves') # Remoção
print(alunos) 
alunos['Kiko'] = 44 # Adiçãode Valor
for nome, mat in alunos.items(): # interando no dicionário
    print(f'Matricula {mat} Nome {nome}') 
alunoscopia = alunos.copy()
alunoscopia['Ana'] = 33
print('Alunos ',alunos)
print('Alunos copia ',alunoscopia) 