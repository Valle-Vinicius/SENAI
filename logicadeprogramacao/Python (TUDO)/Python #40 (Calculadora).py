Valor1 = int(input("Digite um valor!: "))
Valor2 = int(input("Digite um outro valor!: "))

Soma = input("Você deseja somar, multiplicar, dividir, ou subtrair os valores? (Utilize *, +, -, ou /)")

if Soma == "+" or Soma.lower() == "somar":
    print(Valor1+Valor2)
    

elif Soma == "-" or Soma.lower() == "Subtrair":
    print(Valor1-Valor2)

elif Soma == "*" or Soma.lower() == "Multiplicar":
    print(Valor1*Valor2)

elif Soma == "/" or Soma.lower() == "Dividir":

    if Valor1 == 0 or Valor2 == 0:
        print("Erro! Você não pode divir por zero!")

    else:
        print(Valor1 / Valor2)

