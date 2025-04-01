#-*- Coding UTF-8 -*-

# O objetivo dessa programação é o usuário enviar dois números. Caso a soma de ambos números seja maior que 20, ele adiciona +8 no resultado. Caso contrário, subtraia -5 do resultado.

pergunta = int(input("Digite um número: "))
pergunta2 = int(input("Digite um outro número: "))

if pergunta + pergunta2 > 20:
    resultado = pergunta + pergunta2 + 8
    print(f"O Resultado do cálculo é equivalente à : {resultado}")

elif pergunta + pergunta2 <= 20:
    resultado = pergunta + pergunta2 - 5
    print(f"O resultado do cálculo e equivalente à : {resultado}")
 
