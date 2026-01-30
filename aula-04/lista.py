from exercicio_01 import ad_tarefa

nome = "UEA"
alunos = ["Miguel", "Rafael", "Beli", nome]
idades = [18, 19, 20]
Misturado = [ "Ana", 25, True, 1.75]

print(alunos)
print(idades)
print(Misturado)

#acessar elementos na lista
print(alunos[3]) #acessa o quarto elemento da lista alunos
print(idades[0]) #acessa o primeiro elemento da lista idades

#modificar elementos na lista
alunos[3] = 'Unilins' #modifica o quarto elemento da lista alunos
print(alunos)

#adicionar elementos na lista
alunos.append('Carla') #adiciona o elemento Carla no final da lista alunos
print(alunos)

#remover um aluno da lista
alunos.remove("Unilins") #remove o elemento da lista
print(alunos)

print(len(alunos)) #informa quantos elementos existem na lista

for Valuno in alunos:
    print(Valuno)