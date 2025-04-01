salario = float(input("Qual seu salário?: "))

if salario >= 1250:
    ValorS = (salario*10)/100
    ValorT = ValorS + salario
    print(f"O seu salário teve um aumento de 10%, totalizando um salário de: RS${ValorT}")

elif salario <= 1250:
    Valor1 = (salario*15) /100
    Valor2 = Valor1 + salario
    print(f"O seu salário teve um aumento de 15%, totalizando um salário de: RS${Valor2}")
                

