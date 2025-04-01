#-*- Coding UTF-8 -*-

"""
O objetivo dessa programação é o usuário enviar 3 notas e calcular a média. Se a nota for maior que 7 ele é aprovado, menor que 3 reprovado, e o resto é recuperação.
* Entretanto, o diferencial dessa atividade é que ele dá prioridade para falta. Se eu tiver +20 faltas, sou reprovado diretamente por faltas.
"""


faltas = int(input("Digite quantas faltas você tem: "))
nota = float(input("Digite qual suas média: "))
nota2 = float(input("Digite qual suas média: "))
nota3 = float(input("Digite qual suas média: "))
media = nota + nota2 + nota3/3

if faltas > 20:
    print("Reprovado diretamente por faltas")

elif media >= 7:
    print("Aprovado")

elif media <3:
    print("Reprovado")

else:
    print("Recuperação")

