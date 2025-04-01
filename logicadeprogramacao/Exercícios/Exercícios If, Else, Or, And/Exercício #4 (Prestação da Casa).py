ValorDaCasa = float(input("Digite o valor da casa: "))
Salario = float(input("Digite o salário: "))
Anos = int(input("Quantos anos para pagar: "))
Meses = Anos * 12
Prestacao = ValorDaCasa / Meses

if Prestacao > Salario * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {Prestacao} Empréstimo show de bola!!")
