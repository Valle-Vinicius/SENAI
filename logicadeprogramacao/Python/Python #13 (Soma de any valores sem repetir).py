pergunta = int(input("Quantos números você quer somar?"))

grupo = []

for i in range(pergunta):
    valor = int(input("Digite alguns valores"))
    grupo.append(valor)

soma = sum(grupo)


print(f"A soma dos dados é {soma}")
