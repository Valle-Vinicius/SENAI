lista = [-10, -8, 0, 1, 2, 5, -2, -4]

print("")
print("Este programa vai encontrar o maior e o menor número em uma lista de valores.")
print("")

maior = lista[0]  
menor = lista[0]
listastr = str(lista).replace("[", "").replace("]", "")

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("=-"*20)
print(f"Os valores da lista são: {listastr}")
print("=-"*20)
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print("=-"*20)

