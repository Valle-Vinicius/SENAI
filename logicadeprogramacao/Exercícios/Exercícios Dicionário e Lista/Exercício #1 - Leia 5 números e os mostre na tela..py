grupo = []
cont = 1

print("")
print("Este programa irá coletar 5 valores do usuário e, ao final, exibirá esses valores em uma lista formatada.\n")

for i in range(1, 6):
    print(f"===- VALOR NÚMERO {cont} -===\n ")
    valor = int(input(f"{cont}. Digite o valor: "))
    print("")
    grupo.append(valor)
    cont += 1

grupostr = str(grupo).replace("[", "").replace("]", "")
print(f"{grupostr}")
    
