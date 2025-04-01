import time

while True:
    temperatura = int(input("Digite a temperatura do dia: "))
    print("Clima frio!️" if temperatura <20 else "Clima ameno" if temperatura <30 else "Clima quente")
    
    if input("Deseja continuar? Digite 'S' para sair: ").lower() == "s":
        print("Saindo...")
        break
