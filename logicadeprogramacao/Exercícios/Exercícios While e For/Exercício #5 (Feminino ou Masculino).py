# -*- coding: utf-8 -*-

import time

contadorm = 0
contadorf = 0
contadorgeral = 0

time.sleep(1)
print("="*30)
print("Escreva se determinada pessoa é Mulher (F) ou Homem (M)")
print("Atenção: Caso você queira parar a contagem e saber o resultado, escreva 'Sair'")
print("="*30)
print("")

while True:
    valor1 = input("Digite: ")

    if valor1.lower() == "m":
        contadorm += 1
        contadorgeral += 1

    elif valor1.lower() == "f":
        contadorf += 1
        contadorgeral += 1


    elif valor1.lower() == "sair":
        print("="*30)
        print(f"Ao todo, você definiu {contadorgeral} genêros, onde {contadorm} são masculinas, enquanto {contadorf} são femininas...")
        print("Saindo...")
        print("="*30)
        time.sleep(1)
        break

