import sys

lista1 = []
contador = 0
contadorvogais = 0
contadorconsoantes = 0
vogais = []

print("=-" * 20)
print("")
print("Este programa vai pedir para você digitar uma palavra com até 10 letras.")
print("Ele vai contar quantas vogais e consoantes há na palavra e exibir os resultados.\n")
print("=-" * 20)

valor = input("Digite uma palavra de até 10 letras: ")

if valor.isdigit():
    print("Número Inválido! Reinicie o programa para continuar!")
    sys.exit()
    

for i in range(len(valor)):
    contador += 1
    if valor[i] == "a" or valor[i] == "e" or valor[i] == "i" or valor[i] == "o" or valor[i] == "u":
        contadorvogais += 1
        vogais.append(valor[i])
        vogaisstr = str(vogais).replace("[", "").replace("]", "")
    else:
        contadorconsoantes += 1
        lista1.append(valor[i])
        listastr = str(lista1).replace("[", "").replace("]", "")

print("=-" * 20)
print(f"A palavra que você escreveu foi: {valor}, mas somente as consoantes {listastr} foram contabilizadas.")
print(f"A quantidade de vogais é: {contadorvogais}, ou, {vogaisstr}.")
print(f"A quantidade de consoantes é: {contadorconsoantes}, ou, {listastr}.")
print("=-" * 20)
