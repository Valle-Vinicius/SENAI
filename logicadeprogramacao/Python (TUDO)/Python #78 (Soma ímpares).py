def funcao():
    if valor2 >= valor1:
        print("O primeiro valor deve ser maior que o valor secundário")
        return

    grupoimp = []

    for i in range(valor2, valor1):
        if i % 2 != 0:
            grupoimp.append(i)

    soma = sum(grupoimp)
    print(f"A soma de todos os números ímpares entre {valor1} e {valor2} é {soma}")


valor1 = int(input(f"Digite o primeiro número: "))
valor2 = int(input(f"Digite o segundo número: "))
funcao()
