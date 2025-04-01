contador = 0
babilonia = 0

a = int(input("Quantos numeros você quer converter em binário?: "))

for i in range(0, a):
    contador += 1
    babilonia += 1
    teste = bin(babilonia)
    print(f"{contador}. {teste}")
    
