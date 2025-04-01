def eh_palindromo(s):
    return s == s[::-1]

palavra = input("Digite uma palavra")
if eh_palindromo(palavra.lower()):
    print(f"'{palavra}' é um palíndromo!")
else:
    print(f"'{palavra}' não é um palíndromo.")
