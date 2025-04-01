contador = 0

while True:
    valor = int(input("\nDigite até onde você quer saber a contagem: "))

    if valor == -1:
        print("Obrigado! Finalizando o Programa...")
        
    for i in range(1, valor + 1):
        contador += i

    print(f"\n A soma dos valores do número 1, até o valor {valor} é: {contador}")
    contador = 0
    
