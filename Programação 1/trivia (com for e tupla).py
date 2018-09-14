#Perguntas e Respostas:

perguntas = [ ("Qual a capital da Croácia?", "Zagreb"),
             ("Em que ano Python 1.0 tornou-se disponível?", "1994"),
             ("Qual o nome do segundo álbum do Vampire Weekend?" , "Contra"),
             ("Qual o país com mais títulos de Copas do Mundo?", "Brasil"),
              ("Em que ano foi feita a proclamação da república do Brasil?", "1889"),
             ("De qual material é feito o escudo do Capitão América no MUC?", "Vibranuim"),
              ("Qual o verdadeiro nome do Super Homem?", "Clark Kent") ]

NumPerg = 0
pontos = 0

#Início do jogo:

for (pg, rp) in perguntas:
    NumPerg = NumPerg + 1
    print("\n", (NumPerg), "-", pg)
    palpite = input("Palpite: ")
    if palpite == rp:
        print ("Você acertou")
        pontos =  pontos + 1
    else:
        print ("Você errou!")

if pontos == 0:
    print("\n" + "Você não conseguiu pontuar.")
else:
    print ("\n" + "Sua pontuação final foi de ", pontos, "pontos.")

