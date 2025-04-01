soma = []
contador = 0

teste = int(input("Digite quantos valores você quer somar: "))

for i in range(teste):
    contador += 1
    valores = float(input(f"Atualmente você está no número {contador}. Digite o número: "))
    soma.append(valores)

somatotal = sum(soma)

print(f"A soma de todos os números são = {somatotal}")
