# Valores:
meses = int(input("Digite a quantidade de meses: "))
capital = float(input("Digite a capital: "))
taxadejuros = int(input("Digite o juros: "))/100

jurossimples = taxadejuros*capital*meses

print(f"O valor do Juros Simples é de: {jurossimples}")

