grupo = []

for i in range(1, 6):
    valor = int(input("Digite alguns valores"))
    grupo.append(valor)

grupostr = str(grupo).replace("[", "").replace("]", "")
print(f"{grupostr}")
    
