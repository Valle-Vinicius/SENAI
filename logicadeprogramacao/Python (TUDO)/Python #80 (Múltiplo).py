def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

valor = int(input("Digite um valor"))
valor2 = int(input("Digite um outro valor"))

resultado = multiplo(valor, valor2)

if resultado:
    print("os números são multiplicaveis")

else:
    print("não e multiplicavel")
