valor1 = int(input("Quantos dias você alugou o carro?: "))
valor2 = int(input("Quantos KM você rodou: "))

DinheiroPorKM = valor2*0.15 # Sabendo que cada KM rodado, é descontado R$ 0.15, devemos multiplicar quantos KM ele rodou com o valor gasto por KMM
DinheiroPorDias = valor1 * 60 #3 Sabendo que cada dia que passa, é descontado R$ 60, devemos multiplicar a quantidade de dias por 60 reais.
SomaTotal = DinheiroPorKM + DinheiroPorDias

print(f"Ao todo você deve pagar R$ {SomaTotal}, sabendo que você alugou o carro por {valor1} dias, resultando em R$ {DinheiroPorDias}, e mais R$ {DinheiroPorKM}, sabendo que você rodou {valor2} KM's")
