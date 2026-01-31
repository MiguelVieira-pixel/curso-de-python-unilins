def boas_vindas(): # mensagem de boas vindas
    print('Bem vindo ao sistema de cadastro de alunos!')

def saudacao(nome): # saudação
    print(f'olá, {nome}! Seja bem vindo!')

def soma(a,b): # soma
    return a + b

#Chamar a função
boas_vindas()
saudacao('Maria')

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
resultado = soma(numero1,numero2)
print(f'A soma é: {resultado}')

