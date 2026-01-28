#ENTRADA
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

#TABELA DE OPERAÇÕES ARITMÉTICAS
print('\nEscolha a operação aritmética que deseja')
print('+ para somar')
print('- para subtrair')
print('* para multiplicar')
print('/ para dividir')

operador = input('Digite o operador: ') #recebe o operador aritmético e verificar qual operador escolhido
if(operador == '+' or operador == '1'): #adição
    tipo_operacao = "somar"
    resul = num1 + num2
elif(operador == '-' or operador == '2'): #subtração
    tipo_operacao = "subtrair"
    resul = num1 - num2
elif(operador == '*' or operador == '3'): #multiplicação
    tipo_operacao = "multiplicar"
    resul = num1 * num2
else: #divisão
    tipo_operacao = "dividir"
    resul = num1 / num2

#SAIDA
print(f'Você escolheu {tipo_operacao}')
print(f'Resultado: {resul}')


