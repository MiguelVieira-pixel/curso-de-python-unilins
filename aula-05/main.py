# from operacoes import soma, subtracao, multiplicacao, divisao

# a = 12
# b = 0

# print(f'Soma: {soma(a,b)}')
# print(f'Subtração: {subtracao(a,b)}')
# print(f'multiplicação: {multiplicacao(a,b)}')
# print(f'Divisão: {divisao(a,b)}')

from login import login

user = input('Usuário: ')
password = input('Senha: ')
if login(user, password):
    print('Login bem-sucedido.')
else:
    print('Falha no login. Usuário ou senha incorreto.')