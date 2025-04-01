total_menos_21 = 0
total_mais_50 = 0

while True:
    idade = int(input())
    if idade == -99:
        break
    if idade < 21:
        total_menos_21 += 1
    if idade > 50:
        total_mais_50 += 1

print(f'Total de pessoas com menos de 21 anos: {total_menos_21}')
print(f'Total de pessoas com mais de 50 anos: {total_mais_50}')
