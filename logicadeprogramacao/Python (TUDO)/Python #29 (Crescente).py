#-*- Coding UTF-8 -*-

# O objetivo dessa programação é o usuário enviar dois números e, com base nisso, ele colocar ambos números numa ordem crescente. (Do menor número para o maior número)

ordem1 = float(input("Digite um número: "))
ordem2 = float(input("Digite um outro número:"))
grupo = [ordem1, ordem2]
grupo.sort()


if ordem1 == ordem2:
    print("Não tem como colocar essa lista em ordem crescente, visto que os dois números tem valores iguais!")

elif ordem1 != ordem2:
    print(f"A ordem crescente é: {grupo}")

else:
    print("Erro")




