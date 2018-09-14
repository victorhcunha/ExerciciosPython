# Jogo de Adivinhar

numero = int(input("Digite um número a ser adivinhado: "))

while numero <= 0 or numero > 100:
    print ("Seu número deve estar entre '0' e '100'")
    numero = int(input("Digite um número a ser adivinhado: "))

numeroLinha = 50

while numeroLinha > 0:
    print()
    numeroLinha = numeroLinha - 1
    
palpite = int(input("Digite o palpite: "))
tentativas = 0

while tentativas < 2:
    print ("Você errou")
    if palpite > numero:
        print ("Seu palpite foi maior")
        if palpite > numero + 20:
            print ("Muito maior!!")
    if palpite < numero:
        print ("Seu palpite é menor")
        if palpite < numero - 20:
            print ("Muito menor!!")
    tentativas = tentativas + 1
    palpite = int(input("Digite o palpite: "))
    
if palpite == numero:
    print ("Você acertou")
else:
    print ("Você esgotou o número de tentativas")
