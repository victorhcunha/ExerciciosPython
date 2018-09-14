#Perguntas e Respostas:

pergunta = [ "Qual a capital da Croácia?",
             "Em que ano Python 1.0 tornou-se disponível?",
             "Qual o nome do segundo álbum do Vampire Weekend?",
             "Qual o país com mais títulos de Copas do Mundo?",
              "Em que ano foi feita a proclamação da república do Brasil?",
             "De qual material é feito o escudo do Capitão América no MUC?",
              "Qual o verdadeiro nome do Super Homem?"]

resposta = [ "Zagreb",
             "1994",
              "Contra",
              "Brasil",
              "1889",
              "Vibranuim",
              "Clark Kent"]

NumPerg = 0
pontos = 0

#Início do jogo:

print ("Perguntas: ")

while NumPerg < len(pergunta):
    print ("\n", (NumPerg + 1), "-", pergunta[NumPerg])
    r = input("Palpite: ").capitalize()
    if r == resposta[NumPerg]:
        pontos = pontos + 1
        print("Você acertou.")
    else:
        print ("Você errou!")

    NumPerg = NumPerg + 1

print ("\n", "Sua pontuação final foi de", pontos, "pontos")
