# -*- coding: utf-8 -*-

import time
contador = 0
soma = 0

time.sleep(1)
print("="*30)
print("Escreva uma quantidade de números e eu irei te dar uma média sobre todos eles")
print("Atenção: Caso você queira parar a contagem e saber o resultado, escreva 'Sair'")
print("="*30)
print("")

while True:
    valores = input("Digite um número: ").lower()
    
    if valores.isdigit():
        valores = int(valores)
        contador += 1
        soma += valores
        media = soma/contador


    elif valores.lower() == "sair":
        print("="*30)
        print(f"Você inseriu ao todo, {contador} números, totalizando uma soma de: {soma}")
        print(f"A média dos números, no total, é aproximadamente: {media}")
        print("Saindo...")
        print("="*30)
        time.sleep(1)
        break
        
        


        
    
