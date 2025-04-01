def checar_primo():

    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número para verificar se é primo: "))

if checar_primo():
    print(f"{numero} é um primo.")
else:
    print(f"Não e primo.")
