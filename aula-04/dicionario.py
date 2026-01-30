aluno = {
    'nome': 'João',
    'idade': 20,
    'curso': 'Informática'
}

print(aluno)

print(aluno['idade'])

aluno['idade'] = 21 #modifica o item da chave 'idade
print(aluno['idade']) 

aluno['email'] = 'teste@gmail.com' #adicionar uma nova chave-valor ao dicionário
print(aluno)

del aluno['curso'] #remover uma chave-valor do dicionário
print(aluno)

for Vchave, Vvalor in aluno.items():
    print(f'{Vchave}: {Vvalor}')