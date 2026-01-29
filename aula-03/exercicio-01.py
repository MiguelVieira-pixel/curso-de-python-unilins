#entrada de dados
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
frequencia = float(input('Digite a frequência em %: '))

#processamento
media = (nota1 + nota2) / 2 #calculo da média
if(media >= 7 and frequencia >= 75): #aprovado
    resultado = 'Aprovado'
elif(media < 7 and media >= 5) and (frequencia >= 75): #recuperação
    resultado = 'Recuperação'
else: #reprovado
    resultado = 'Reprovado'

#saída de dados
print(f'Nome: {nome}')
print(f'Media final: {media}')
print(f'Frequencia: {frequencia}')
print(f'Situação: {resultado}')
