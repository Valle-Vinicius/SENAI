idade = int(input("Digite a idade: "))

if idade < 2:
    print("Você é um bebê")

elif idade >= 2 and idade < 12:
    print("Você e uma criança")

elif idade >= 12 and idade < 23:
    print("Você é um adolescente")

elif idade >= 23 and idade < 70:
    print("Você e um adulto")

elif idade > 70:
    print("Você é um idoso")

else:
    print("Erro!")
