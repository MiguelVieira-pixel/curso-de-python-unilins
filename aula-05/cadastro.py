students = []

while True:
    print('\n ------------------SISTEMA DE ALUNOS------------------')
    print('1 - Cadastrar aluno')
    print('2 - listar aluno')
    print('3 - buscar aluno pelo nome')
    print('4 - sair')

    option = int(input('Escolha uma opção: '))
    
    #opção 1 - cadastrar
    if option == 1:
        name = input('Nome completo: ')
        age = input('Idade: ')
        course = input('Curso: ')

        student = {
            'nome': name,
            'idade': age,
            'curso': course
        }

        students.append(student)
    
    #opção 2 - listar
    elif option ==2:
        if len(students) == 0:
            print('Nenhum aluno cadastrado.')
        else:
            print('---- LISTA DE ALUNOS ---- \n')
            print('----------------------------------------')
            for student in students:
                print(f'{student['name']:<20} {student['age']:<10} {student['course']:<15}')
            # print(f'{name:<20} {age:<10} {course:<15}')
            print('----------------------------------------')



    #opção 3 - buscar
    elif option == 3:
        search = input('Digite o nome do aluno: ')
        finded = False

        for student in students:
            if student[name].lower() == search.lower():
                print(f'Aluno encontrado: {student}')
                finded = True

        if not finded:
            print('Aluno não encontrado.')

    #opção 4 - sair
    elif option == 4:
        print('Encerrando o sistema.')
        break

    else:
        print('Opção inválida')
    