# -*- coding: utf-8 -*-

import time

contador12 = 0
contador = 0
grupo1020 = []
contadornum = 1

time.sleep(1)
print("="*30)
print("Escreva uma quantidade de números e eu irei te dar uma contagem avançada sobre eles")
print("Atenção: Caso você queira parar a contagem e saber o resultado, escreva 'Sair'")
print("="*30)
print("")

while True:
    valor1 = input("Digite um número (ou '0' para encerrar): ")

    if valor1.isdigit():
        valor1 = int(valor1)

        if valor1 != 0:
            contador += 1

        if valor1 >= 100 and valor1 <= 200:
            contador12 += 1
            grupo1020.append(valor1)

        elif valor1 == 0:
            print("="*30)
            print(f"Ao todo você falou {contador} números, sendo que deles, {contador12} estão entre 100 e 200.")
            print(f"Os números que você falou, que estão entre 100 e 200 são os seguintes números:")

            for numero in grupo1020:
                print(f"{contadornum}. {numero}")
                contadornum += 1
            print("="*30)
            break
