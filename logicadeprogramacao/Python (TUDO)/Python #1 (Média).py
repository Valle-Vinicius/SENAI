valor1 =int(input("Digite a primeira nota"))
valor2 =int(input("Digite a segunda nota"))
valor3 =int(input("Digite a terceira nota"))
media = (valor1 + valor2 + valor3) / 3

if media >= 0 and media <= 4:
	print("você foi reprovado sem possível recuperação")
else:
  if media >4 and media <7:
    print("sua média foi média mas com possível recuperação")

if media >=7 and media <10:
    print("sua média foi, você foi aprovado")
    
else: 
    print("o que você fez de errado?")


