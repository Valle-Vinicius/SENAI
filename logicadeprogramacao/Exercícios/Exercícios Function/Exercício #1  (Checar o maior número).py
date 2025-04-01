def maior_numero():
    if numero1 > numero2:
        return numero1
    else:
        return numero2

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

maior = maior_numero()
print(f"O maior número é: {maior}")
