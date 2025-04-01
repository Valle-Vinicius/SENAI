ValorTotal = float(input("Digite o valor do produto em reais do produto: "))
Porcentagem = int(input("Digite a porcentagem de desconto do produto: "))

ValorS = (ValorTotal*Porcentagem)/100
SalarioN = ValorTotal - ValorS

print(f"O produto teve um desconto de {ValorS} , totalizando um valor de R$ {SalarioN}") 
