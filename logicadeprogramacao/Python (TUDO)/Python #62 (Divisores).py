valor = int(input("Digite um valor: "))

for i in range(1, valor + 1):
    if valor % i == 0:
        print(i)
