def funcao():
    if valor <0:
        print("O valor é negativo, então logo o resultado é \nN")
    elif valor > 0 or valor == 0:
        print("O valor é positivo, então logo o resultado é: \nP")


valor = float(input("Digite um valor"))
resultado = funcao()

