import time

segundos = 0
minutos = 0
horas = 0

while True:
    segundos += 1
    
    if segundos == 60:
        minutos += 1
        segundos = 0
    
    if minutos == 60:
        horas += 1
        minutos = 0
        
    time.sleep(1)
    
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
