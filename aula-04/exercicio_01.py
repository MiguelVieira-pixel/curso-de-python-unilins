tarefas = []
# adiciona um elemento na lista tarefas
def ad_tarefa(Ptarefa):
    tarefas.append(Ptarefa) 
    print(f'Tarefa {Ptarefa} adicionada')


# remove um elemento na lista tarefas
def rm_tarefa(Ptarefa):
    if Ptarefa in tarefas:
        tarefas.remove(Ptarefa)
        print(f'Tarefa {Ptarefa} removida')
    else:
        print(f'Tarefa {Ptarefa} não encontrada')


# mostrar os elementos da lista
def li_tarefas():
    print('Lista de tarefas: ')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')

#Código
ad_tarefa("acordar")
ad_tarefa("acordar")
rm_tarefa('acordar')
li_tarefas()