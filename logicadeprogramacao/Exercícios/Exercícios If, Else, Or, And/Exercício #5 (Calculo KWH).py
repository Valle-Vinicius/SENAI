import time

while True:
    time.sleep(3)
    valor = input("Digite o seu tipo de residência (Residencial, Comercial, Industrial): ")

    if valor.lower() == "residencial":
        faixa1 = int(input("Digite sua Faixa de KWH: "))
        if faixa1 <= 500:
            valorr500 = faixa1 * 0.40
            print(f"Você deve pagar R$ {valorr500}")
        elif faixa1 > 500 and faixa1 <= 1000:
            valorr1000 = faixa1 * 0.65
            print(f"Você deve pagar R$ {valorr1000}")

    elif valor.lower() == "comercial":
        faixa1 = int(input("Digite sua Faixa de KWH: "))

        if faixa1 <= 2500:
            valorc2500 = faixa1 * 0.55
            print(f"Você deve pagar R$ {valorc2500}")

        elif faixa1 > 2500 and faixa1 < 5000:
            valorc5000 = faixa1 * 0.60
            print(f"Você deve pagar R$ {valorc5000}")

    elif valor.lower() == "industrial":

        faixa1 = int(input("Digite sua Faixa de KWH: "))
        if faixa1 < 10000:
            valori10000 = faixa1 * 0.55
            print(f"Você deve pagar R$ {valori10000}")
        elif faixa1 >= 10000 and faixa1 < 15000:
            valori15000 = faixa1 * 0.60
            print(f"Você deve pagar R$ {valori15000}")
