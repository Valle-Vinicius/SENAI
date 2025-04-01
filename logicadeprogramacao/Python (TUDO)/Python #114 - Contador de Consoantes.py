lista1 = []
contador = 0
contadorvogais = 0
contadorconsoantes = 0
vogais = []

valor = input("Digite uma palavra de até 10 letras: ")

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

print(f"A palavra que você escreveu foi {valor}, mas somente as consoantes {listastr} foram contabilizadas")
print(f"A quantidade de vogais são {contadorvogais}, ou, {vogaisstr}")
print(f"A quantidade de consoantes são {contadorconsoantes}, ou, {listastr}")


