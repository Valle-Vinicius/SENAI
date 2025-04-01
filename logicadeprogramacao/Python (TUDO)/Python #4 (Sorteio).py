import random

Teste = input("Escolha o nome do primeiro aluno")
Teste2 = input("Escolha o nome do segundo aluno")
Teste3 = input("Escolha o nome do terceiro aluno")
Teste4 = input("Escolha o nome do quarto aluno")
Teste5 = input("Escolha o nome do quinto aluno")
Teste6 = input("Escolha o nome do sexto aluno")
Teste7 = input("Escolha o nome do sétimo aluno")
Teste8 = input("Escolha o nome do oitavo aluno")
lista = [Teste, Teste2, Teste3, Teste4, Teste5, Teste6, Teste7, Teste8]

sorteio = random.choice(lista)
print("o aluno sorteado foi", sorteio)


