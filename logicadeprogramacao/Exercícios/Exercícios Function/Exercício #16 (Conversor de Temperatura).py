def convertor():
    escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").upper()
    
    if escolha == 'C':
        celsius = int(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"A temperatura em Celsius é: {celsius}°C")
        print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
    
    elif escolha == 'F':
        fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")
        print(f"A temperatura em Celsius é: {celsius:.2f}°C")
    
    else:
        print("Opção inválida! Por favor, digite 'C' ou 'F'.")

convertor()
