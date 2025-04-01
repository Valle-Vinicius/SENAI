grupo = []
contador = 1

for i in range(1, 11):
    valores = int(input(f"{i} Digite um valor: "))
    grupo.append(valores)

valorcontrario = grupo[::-1]
valorstr = str(valorcontrario).replace("[", "").replace("]", "")

print(f" Os números em ordem reversa são: {valorstr}")
    
    
