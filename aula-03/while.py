# num1 = 1
# num2 = 4
# resultado = 0.0

# while(num1 <= 9):

#     resultado = num1 * num2
#     print(f'{num1} x {num2} = {resultado}')
#     num1 += 1

# print('Laço encerrado.')

nome = None
while True:
    print('Digite seu nome ou x para  sair: ')
    nome = input()

    if nome == 'x' or nome == 'X':
        break
    else:
        print(f'Olá {nome}, seja bem vindo!')

print('Laço encerrado.')
        
