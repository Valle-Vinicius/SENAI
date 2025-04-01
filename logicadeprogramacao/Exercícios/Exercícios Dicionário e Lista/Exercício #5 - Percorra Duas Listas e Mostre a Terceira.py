print("")
print("Este programa vai combinar os dois primeiros valores de duas listas em uma nova lista.")

lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 10, 15, 20, 25]
lista3 = []

lista1str = str(lista1).replace("[", "").replace("]", "")
lista2str = str(lista1).replace("[", "").replace("]", "")

lista3.extend(lista1[:2])
lista3.extend(lista2[:2])
listastr = str(lista3).replace("[", "").replace("]", "")

print("")
print("=-"*20)
print(f"Os valores da Lista 1 são: {lista1str}")
print(f"Os valores da Lista 2 são: {lista2str}")
print("=-"*20)
print(f"Os valores da lista três são: {listastr}")
print("=-"*20)




    
