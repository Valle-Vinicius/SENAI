def teste():
    if soma == "+":
        resultado = valor + valor2
        print(resultado)
    elif soma == "-":
        resultado = valor - valor2
        print(resultado)
    elif soma == "/":
        resultado = valor / valor2
        print(resultado)
    elif soma == "*":
        resultado = valor * valor2
        print(resultado)
        


valor = int(input("Digite um valor"))
valor2 = int(input("Digite outro valor"))
soma = input("Digite +, -, /, ou *")
teste()
