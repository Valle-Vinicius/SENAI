notas = []
contador = 1

for i in range(1, 5):
    valores = int(input(f"{contador}. Digite suas notas: "))
    contador += 1
    notas.append(valores)

media = sum(notas)/len(notas)

print(f"A média dos números e equivalente à {media}")
