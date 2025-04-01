#-*- coding: UTF-8 -*-

# Primeiro exercício da Lógica de Programação e Algoritmo
# Atividade Um:

import time

print("Esse programa fará o calculo da soma de dois valores!")
soma1 = float(input("Digite um valor: "))
soma2 = float(input("Digite um outro valor: "))
soma3 = soma1 + soma2

print("🎲 Analisando")
time.sleep(1.5)
pergunta = input("Você quer saber a soma desses valores? ")

if pergunta.lower() == 'sim':
    print("🎲 Analisando")
    time.sleep(1.5)
    print(f"A soma dos dois valores é {soma3}")
