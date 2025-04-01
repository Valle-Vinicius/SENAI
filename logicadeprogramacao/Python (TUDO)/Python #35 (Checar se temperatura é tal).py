import time

while True:
    temperatura = input("🧩 Digite a temperatura do dia: ")

    if temperatura.isdigit():
        temperatura = int(temperatura)
        if temperatura < 20:
            print("Clima frio! 🥶🌬️")
        elif 20 <= temperatura < 30:
            print("Clima ameno! 🌤️😊")
        else:
            print("Clima quente! ☀️🔥")
    else:
        print("Insira um número válido para a temperatura. ⚠️")
    
    time.sleep(1)

    continuar = input("Deseja continuar? Então clique enter! (Digite 'S' para sair): ")
    
    if continuar.lower() == "s":
        print("Saindo do programa... 👋")
        time.sleep(1)
        break
    elif continuar != "S":
        continue