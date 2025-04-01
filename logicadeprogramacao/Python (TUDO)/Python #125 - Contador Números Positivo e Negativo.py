contadornegativo = 0
contadorpositivo = 0
contadorgeral = 0 

while True:
    valor = int(input("Digite alguns valores e, caso queira parar, digite '0': "))

    if valor == 0:
        print("")
        print(f"Ao todo você inseriu {contadorgeral}, sendo deles:\n Números Positivos: {contadorpositivo}\n Números Negativos: {contadornegativo}")
        break

    elif valor > 0:
        contadorgeral += 1
        contadorpositivo += 1

    elif valor < 0:
        contadorgeral += 1
        contadornegativo += 1
