valor = int(input("Digite o tamanho do triângulo: "))

for i in range(1, valor+1):
    print(f"{'*' * i}".center(valor*1))
