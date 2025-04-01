# -*- coding: UTF-8 -*-
print("======== CONVERSÃO EM SEGUNDOS ========")
      
Dias = int(input("Digite a quantidade de dias: "))
Hora = int(input("Digite a quantidade de horas: "))
Minutos = int(input("Digite a quantidade de minutos: "))
Segundos = int(input("Digite a quantidade de segundos: "))

ConversaoD = Dias*86400
ConversaoH = Hora*3600
ConversaoM = Minutos*60

TempoTotal = ConversaoD + ConversaoH + ConversaoM + Segundos

print(f"O tempo total que você escreveu, convertido para segundos, é equivalente à {TempoTotal} segundos")
