maior = float('-inf')
menor = float('inf')


    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
