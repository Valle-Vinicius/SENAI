num1 = int(input("Digite um número"))
num2 = int(input("Digite um outro número"))

if num1 % num2 == 0:
    print(f"O número {num1} é divisível por {num2}")

elif num1 % num2 != 0:
    print(f"O número {num1} não é divisível por {num2}")
else:
    print("Erro!")
    
