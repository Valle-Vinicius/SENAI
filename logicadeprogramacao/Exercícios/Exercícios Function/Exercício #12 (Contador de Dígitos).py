contador = 1

def multiplicar(valor):
    global contador
    for i in valor:
        contador *= int(i)

        if contador == 0:
            print("A contagem vai parar pois o número há um 0, então o resultado sempre vai ser 0")
            break

valor = input("Digite um valor: ")
multiplicar(valor)

print(f"O resultado da multiplicação é: {contador}")




