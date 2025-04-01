import time

while True:
    temperatura = int(input("🧩 Digite a temperatura do dia: "))

    if temperatura <= 15:
        print("Muito frio")

    elif temperatura >= 16 and temperatura < 23:
        print("Frio")

    elif temperatura >= 23 and temperatura < 26:
        print("Agradável")

    elif temperatura >= 26 and temperatura < 30:
        print("Calor")

    elif temperatura >= 31:
        print("Muito quente")

    else:
        print("Erro")
