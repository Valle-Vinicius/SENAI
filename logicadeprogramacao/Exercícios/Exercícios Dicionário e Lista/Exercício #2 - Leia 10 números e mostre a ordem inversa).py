grupo = []
contador = 1
cont = 1

print("")
print("Este programa irá coletar 10 valores do usuário e, ao final, exibirá esses valores em ordem reversa.\n")

for i in range(1, 11):
    print(f"===- VALOR NÚMERO {cont} -===\n ")
    valores = int(input(f"{i}. Digite um valor: "))
    print("")
    grupo.append(valores)
    cont += 1

valorcontrario = grupo[::-1]
valorstr = str(valorcontrario).replace("[", "").replace("]", "")

print(f" Os números em ordem reversa são: {valorstr}")
    
    
