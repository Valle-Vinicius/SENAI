altura = []
idade = []
cont = 1

print("")
print("Este programa irá coletar as alturas e idades de 5 usuários.")
print("Em seguida, ele exibirá as listas de alturas e idades de trás para frente,")
print("com as alturas arredondadas para o número inteiro mais próximo.\n")

for i in range(1, 6):
    print(f"===- USUÁRIO NÚMERO {cont} -===\n ")
    alturas = float(input(f"{cont}. Digite a altura! "))
    altura.append(alturas)
    idades = int(input(f"{cont}. Digite a idade! "))
    print("")
    idade.append(idades)
    cont += 1

alturainversa = altura[::-1]
idadeinversa = idade[::-1]

alturastr = str(alturainversa).replace("[", "").replace("]", "")
idadestr = str(idadeinversa).replace("[", "").replace("]", "")


print(f"A Lista de Alturas são: {alturastr}")
print(f"A Lista de Idades são: {idadestr}")
