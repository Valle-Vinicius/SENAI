notas = []
contador = 1
print("")
print("Este programa irá coletar 4 notas do usuário e calcular a média dessas notas.\n")

for i in range(1, 5):
    print(f"===-VALOR NÚMERO {contador}-===\n")
    valores = float(input(f"{contador}. Digite suas notas: "))
    print("")
    contador += 1
    notas.append(valores)

media = sum(notas)/len(notas)

print("=-"*40)
print(f"A média dos números e equivalente à {media}")
