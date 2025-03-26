def contString(frase):

    import string

    palavra = frase.split()#divide a frase
    letra1 =[letra.lower() for letra in frase if letra.isalpha()]#Conta as letras como a b c etc

    contapalavra = len(palavra)#soma
    contaletra = len(letra1)#soma
    vazio = frase.count(" ")#soma os espacos 
    especiais = [char for char in frase if char in string.punctuation]#Conta os caracteres especias como ! * ^ & etc
    contaespeciais = len(especiais)

    print(f"Sao {contapalavra} palavras!") 
    print(f"Sao {contaletra} letras!")
    print(f"Sao {vazio} espacos vazios!")
    print(f"Sao {contaespeciais} caracteres especiais!")

    return contString