ValorTotal = float(input("Digite seu novo salário: "))
Porcentagem = int(input("Digite a porcentagem de aumento do seu salário: "))

ValorS = (ValorTotal*Porcentagem)/100
SalarioN = ValorTotal + ValorS

print(f"O seu salário teve um aumento de {ValorS} , totalizando um salário de {SalarioN}") 
