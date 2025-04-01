numero = int(input("Digite quantos salários você quer somar"))
salarios = []

for i in range(numero):
    salario = int(input("Digite o salário"))
    salarios.append(salario)
    
soma = sum(salarios)

pergunta = input("Você quer descobrir qual é a soma dos seus salários?")

if pergunta.lower() == "sim":
    print(f"A soma de todos seus salários é R$ {soma}")
