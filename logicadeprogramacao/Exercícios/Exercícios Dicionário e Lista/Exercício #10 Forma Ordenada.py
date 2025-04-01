print("")
print("Este programa irá ordenar uma lista de números de forma crescente.")
print("Após ordenar, ele exibirá os números na ordem correta, sem colchetes e vírgulas.\n")

L = [9, 8, 7, 12, 0, 13, 21]
Lista = [9, 8, 7, 12, 0, 13, 21]

L.sort()
lstr = str(L).replace("[", "").replace("]", "")
Listastr = str(Lista).replace("[", "").replace("]", "")


print("=-=" * 20)
print(f"A Lista original é {Listastr}")
print(f"A ordem ordenada dos números são: {lstr}")
print("=-=" * 20)
