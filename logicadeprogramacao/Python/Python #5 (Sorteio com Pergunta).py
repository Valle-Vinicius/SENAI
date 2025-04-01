import random

Teste = input("Escolha o nome do primeiro aluno: ")
Teste2 = input("Escolha o nome do segundo aluno: ")

lista = [Teste, Teste2]


teste11 = input("Você quer sortear agora?")
if teste11 == 'sim' or teste11 ==  'Sim':
    sorteio = random.choice(lista)
print("o aluno sorteado foi", sorteio)


