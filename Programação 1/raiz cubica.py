#Calcular raiz cúbica
# n = Resultado

print ("Cálculo da raiz cúbica")
N = int(input("Digite um número: "))
n = 1
nnn = n*n*n

while (n*n*n) != N:
    n = n + 1
    nnn = n*n*n
    if nnn > N or nnn == N:
        break
    
if (n*n*n) == N:
    print (n)
else:
    print ("Não há resultado inteiro")
