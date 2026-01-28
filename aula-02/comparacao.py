#VARIAVEIS
x = y = z = False
num1 = num2 = 0

#ENTRADA
num1 = int(input('Informe um número:'))
num2 = int(input('Informe outro número: '))

#SAIDA
x = num1 == num2 #verifica se num1 e num2 são iguais
print('\nSão iguais?', x, '\n')

y = num1 > num2
print(f'{num1} é maior que {num2}? {y}\n')

z = num1 != num2
print(f'{num1} é diferente de {num2}? {z}\n')