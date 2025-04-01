import random
import time

# Coletando os nomes dos alunos
Teste = input("🎲 Escolha o nome do primeiro aluno:")
Teste2 = input("🎲 Escolha o nome do segundo aluno: ")
Teste3 = input("🎲 Escolha o nome do terceiro aluno: ")
Teste4 = input("🎲 Escolha o nome do quarto aluno: ")
Teste5 = input("🎲 Escolha o nome do quinto aluno: ")
Teste6 = input("🎲 Escolha o nome do sexto aluno: ")
Teste7 = input("🎲 Escolha o nome do sétimo aluno: ")
Teste8 = input("🎲 Escolha o nome do oitavo aluno: ")

lista = [Teste, Teste2, Teste3, Teste4, Teste5, Teste6, Teste7, Teste8]

while True:
    teste11 = input("Você quer sortear agora? (sim/não): ")

    if teste11.lower() == 'sim':
        print("Aguardando... 🎲")
        time.sleep(1)
        sorteio = random.choice(lista)
        print("🎉 O aluno sorteado foi:", sorteio)
        
    elif teste11.lower() == 'não':
        print("😱 Oloco, então por que você executou esse comando? Quero saber... Vou explodir em 3 segundos... ⏳")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("BOOOOM!!! 💥 *efeito sonoro de explosão*")
        
    else:
        print("Resposta inválida! Tente novamente.")

    continuar = input("Deseja sortear? (sim/não): ").lower() ## Tira a chance da pessoa escrever variáveis de "Sim" ou "Não"
    if continuar != 'sim':
        print("Ok, sorteio finalizado!")
        break
    else:
        print("Vamos sortear de novo! 🎉")

print("Espero que tenha se divertido! Até a próxima! 👋")
