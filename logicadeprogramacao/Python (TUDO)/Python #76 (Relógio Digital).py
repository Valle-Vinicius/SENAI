import datetime
import time

while True:
    hora_atual = datetime.datetime.now()
    hora_formatada = hora_atual.strftime("%H:%M:%S")
    print(hora_formatada)
    time.sleep(1)
    
