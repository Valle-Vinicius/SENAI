def contar_digitos(numero):
    contador = 0
    while numero > 0:
        numero //= 10
        contador += 1
    print(contador)


numero = int(input("Digite um número: "))

contar_digitos(numero)
