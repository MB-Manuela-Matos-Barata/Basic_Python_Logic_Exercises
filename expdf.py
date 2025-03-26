#5. Escreva um programa que lê uma quantia inteira de euros e mostra como pagar essa 
# quantia em notas de 20€, 10€, 5€ e moedas de 1€.
# Exemplo: Qual a quantia em €? 89 notas 20€: 4 notas 10€: 0 notas 5€: 1 

valor = int(input("Digite o valor em €:\t"))

while valor <=0:
    print("ERRO - VALOR INVALIDO")
    valor = int(input("Digite o valor em €:\t"))
else:   
    if valor >= 1:
        notas20= int(valor/20)
        resto20= int(valor%20)
        notas10=int(resto20/10)
        resto10=int(resto20%10)
        notas5=int(resto10/5)
        resto5=int(resto10%5)
        notas1=int(resto5/1)
        resto1=int(resto5%1)
        print(f"Voce precisa de {notas20} notas de 20")
        print(f"Voce precisa de {notas10} notas de 10")
        print(f"Voce precisa de {notas5} notas de 5")
        print(f"Voce precisa de {notas1} notas de 1")
    else:
        print("ERRO - VALOR INVALIDO")