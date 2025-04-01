Prestacao = float(input("Digite o valor da prestação: "))
Salario = float(input("Digite o salário: "))


if Prestacao > Salario * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {Prestacao} Empréstimo show de bola!!")
