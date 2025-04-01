import time
saldo = 10000

time.sleep(2)

print("="*50)
print(" "*20, "Bom dia!")
print("="*50)

time.sleep(2)
print("="*30)
print("📌 O que você gostaria de checar?: ")
print("="*30)
time.sleep(1)

while True:
    time.sleep(2)
    print("="*30)
    print("1️⃣ - Checar seu saldo!") 
    print("2️⃣ - Depositar determinado valor") 
    print("3️⃣ - Retirar determinado valor") 
    print("4️⃣ - Sair") 
    print("="*30)
    
    pergunta = int(input("🉐 Determine o número correspondente!: "))

    if pergunta == 1:
        time.sleep(1)
        print("Analisando... 🤖")
        time.sleep(1)
        print(f" ✅  Você tem atualmente R$ {saldo}")
        
    elif pergunta == 2:
        time.sleep(2)
        depositarsaldo = float(input("🧠 Quanto de saldo você quer depositar em sua conta?: "))
        saldo += depositarsaldo
        
        time.sleep(1)
        print("Analisando... 🤖")
        time.sleep(1)
        
        print(f"✅ Sucesso, agora você possui R$ {saldo}")  
        
    elif pergunta == 3:
        time.sleep(2)
        retirarsaldo = float(input("🧠 Quanto de saldo você quer retirar?: "))
        
        if retirarsaldo <= saldo:
            saldo -= retirarsaldo
            time.sleep(2)
            print("Analisando... 🤖")
            time.sleep(1)
            print(f"✅ Sucesso, agora você possui R$ {saldo}")  
        
        elif retirarsaldo < 0:
            print("❌ Você tem que retirar ao menos R$ 1")
            
        else:
            print("Erro!")
            
    elif pergunta == 4:
        time.sleep(1)
        print("🧠 Ok! Até mais tarde")
        break
