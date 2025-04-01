valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite um outro número: "))

if valor1 > valor2:
    print(f"O valor {valor1} é maior que o {valor2}")

elif valor1 < valor2:
    print(f"O valor {valor2} é maior que o {valor1}")

elif valor1 == valor2:
    print("Os dois números tem o mesmo valor")

else:
    print("Erro")
