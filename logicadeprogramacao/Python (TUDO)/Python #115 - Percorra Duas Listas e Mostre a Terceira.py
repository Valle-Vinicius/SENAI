lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 10, 15, 20, 25]
lista3 = []

lista3.extend(lista1[:2])
lista3.extend(lista2[:2])
listastr = str(lista3).replace("[", "").replace("]", "")

print(f"Os valores da lista três são: {listastr}")



    
