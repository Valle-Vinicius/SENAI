num1 = int(input("Digite quantas horas você trabalhou: "))
salario = num1 * 19.50

if salario > 1500:
    impostoderenda = salario * 0.10
    salariodescontado = salario - impostoderenda
    print(f"Descontamos R$ {impostoderenda} do seu salário por conta do imposto de renda, 10%, totalizando um salário de {salariodescontado}")

else:
    print("O seu salário total é: {salario}, sem ser descontado em relação ao imposto de renda")
    
    
