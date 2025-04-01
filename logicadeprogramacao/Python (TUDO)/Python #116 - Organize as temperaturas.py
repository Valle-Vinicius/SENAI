lista = [-10, -8, 0, 1, 2, 5, -2, -4]

maior = lista[0]  
menor = lista[0]  

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
