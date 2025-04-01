# -*- coding: utf-8 -*-

import time

contador = 0

time.sleep(1)
print("="*30)
print("Escreva uma quantidade de números e eu irei proclamar quantos números você escreveu")
print("Atenção: Caso você queira parar a contagem e saber o resultado, escreva 'Sair'")
print("="*30)
print("")

while True:
    valores = input("Digite um número: ").lower()
    
    if valores.isdigit():
        valores = int(valores)
        contador += 1


    elif valores.lower() == "sair":
        print("="*30)
        print(f"Você inseriu ao todo, {contador} números")
        print("Saindo...")
        print("="*30)
        break
    
