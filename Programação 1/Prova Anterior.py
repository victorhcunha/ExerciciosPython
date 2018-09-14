#1 Questão

def formatar (a):
    if temEspaco(a) == False:
        return [a]
    primeira = pegarPrimeiraPalavra(a)
    segunda = descartarPrimeiraPalavra(a)
    return [primeira] + formatar(segunda)

def pegarPrimeiraPalavra(palavra):
    if temEspaco(palavra) == False:
        return palavra
    else:
        palavra = list(palavra)
        i = ""
        for x in palavra:
            if x == " ":
                break
            else:
                i = i + x
        return i
    
def descartarPrimeiraPalavra(palavra):
    if temEspaco(palavra) == False:
        return palavra
    else:
        palavra = list(palavra)
        i = ""
        contador = 0
        for x in palavra:
            contador = contador + 1
            if x == " ":
                break
        for x in palavra[contador:]:
            if x == "":
                break
            else:
                i = i + x
        return i

def temEspaco(palavra):
    palavra2 = list(palavra)
    test = False
    for i in palavra:
        if i == " ":
            test = True
    return test

