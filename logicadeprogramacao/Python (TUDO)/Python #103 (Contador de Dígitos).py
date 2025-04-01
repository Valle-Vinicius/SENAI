contador = 1

def multiplicar(valor):
    global contador
    for i in range(1, valor + 1):  
        contador *= i

valor = int(input("Digite um valor: "))
multiplicar(valor)

print(f"O resultado da multiplicação é: {contador}")


