
h = open ("perguntas.txt", "r")
i = open ("respostas.txt", "r")

listaRespostas = i.readlines()[:]

listaRespostas = [x[: len(x) - 1] for x in listaRespostas]

f = 0


while f == 0:
    pontos = 0
    contador = -1
    print("\n Início")
    jogador = input("Digite seu nome: ")
    h.seek(0)
    for linha in h:
        contador = contador + 1
        print("\n",contador + 1,"-",(linha[: len(linha) - 1]))
        palpite = input()
        if palpite == listaRespostas[contador]:
            pontos = pontos + 1
            print("Você acertou. \n")
        else:
            print ("Você errou! \n")
    if pontos == 1 or pontos == 0:
        print ("\n", "Sua pontuação final foi de", pontos, "ponto")
    else:
        print ("\n", "Sua pontuação final foi de", pontos, "pontos")

    d = open ("pontuação.txt", 'a')
    d.write(jogador+": "+str(pontos)+"\n")
    f = 0
    d.close()

