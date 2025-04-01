valores = [9, 8, 7, 12, 0, 13, 21]
cont = 1
valoresstr = str(valores).replace("[", "").replace("]", "")


print("-="*35)
print("Este programa vai verificar se cada número em uma lista é par ou ímpar.")
print(f"Os valores da lista é: {valoresstr}")


print("-="*35)
for i in valores:
    if i % 2 == 0:
        print(f"{cont}. O número {i} é par!")
        cont += 1
    elif i % 2 != 0:
        print(f"{cont}. O número {i} é ímpar!")
        cont += 1
print("-="*20)

