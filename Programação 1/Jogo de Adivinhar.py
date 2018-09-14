# Jogo de Adivinhar 
# J1 = Jogador1; J2 = Jogador2 
 
 
print ("Jogador 1 indique um número a ser advinhado") 
J1 = int(input()) 
 
 
print ("\n"*60) 
 
 
print ("Jogador 2, você tem três chances para tentar adivinhar") 
J2 = int(input()) 
 
 
if J2 == J1: 
    print ("Parabéns, você conseguiu") 
 
 
if J2 > J1: 
    print ("Seu número foi maior") 
 
 
if J2 < J1: 
    print ("Seu número foi menor") 
 
 
if J2 != J1: 
    print ("Tente novamente") 
    J2 = int(input()) 
     
    if J2 == J1: 
        print ("Parabéns, você conseguiu") 
 
 
    if J2 > J1: 
        print ("Seu número foi maior") 
 
 
    if J2 < J1: 
        print ("Seu número foi menor") 
         
    if J2 != J1: 
        print ("Última chance") 
        J2 = int(input()) 
          
        if J2 == J1: 
            print ("Parabéns, você conseguiu") 
 
 
        if J2 > J1: 
            print ("Seu número foi maior") 
 
 
        if J2 < J1: 
            print ("Seu número foi menor") 
              
        if J2 != J1: 
            print ("Você perdeu") 
 
 
 
