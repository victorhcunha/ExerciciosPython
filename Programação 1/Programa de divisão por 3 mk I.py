Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Programa que lê entre 100 e 99
# N = Número dado

N = int(input("Digite um número entre 100 e 999:  "))
while N > 999 and N < 100:
    N = int(input())

N%3 == 0
