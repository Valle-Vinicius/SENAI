grupo = []

while True:
    pergunta = int(input("Digite alguns números:"))
    grupo.append(pergunta)

    if pergunta <= 0:
        sum(grupo)
        print(f"A soma dos valores totais é equivalente à: {pergunta}")
        break
