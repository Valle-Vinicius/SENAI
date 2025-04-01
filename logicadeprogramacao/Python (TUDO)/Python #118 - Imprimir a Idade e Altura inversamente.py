altura = []
idade = []

for i in range(1, 6):
    alturas = float(input("Digite a altura!"))
    altura.append(alturas)
    idades = int(input("Digite a idade!"))
    idade.append(idades)

alturainversa = altura[::-1]
idadeinversa = idade[::-1]

alturastr = str(alturainversa).replace("[", "").replace("]", "")
idadestr = str(idadeinversa).replace("[", "").replace("]", "")


print(f"A Lista de Alturas são: {alturainversa}")
print(f"A Lista de Idades são: {idadeinversa}")
