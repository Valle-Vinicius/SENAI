def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

maior = maior_numero(numero1, numero2)
print(f"O maior número é: {maior}")
