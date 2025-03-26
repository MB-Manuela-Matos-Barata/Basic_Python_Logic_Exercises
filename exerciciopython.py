frase = str(input("Digite uma frase: "))

palavra = frase.split()
letra1 =[letra.lower() for letra in frase if letra.isalpha()]

contapalavra = len(palavra)
contaletra = len(letra1)

print(f"Sao {contapalavra} palavras!") 
print(f"Sao {contaletra} letras!")
