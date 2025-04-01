grupopares = []
grupoimpares = []

while True:
    valor = input("Digite um número (ou 1000 para sair): ")

    valor = int(valor)

    if valor == 1000:
        break

    if valor % 2 == 0:
        grupopares.append(valor)

    elif valor % 2 != 0:
        grupoimpares.append(valor)

somai = sum(grupoimpares)
somap = sum(grupopares)

print(f"A soma dos valores ímpares é {somai} e a soma dos valores pares é {somap}")
