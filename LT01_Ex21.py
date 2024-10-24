# Objetivo: Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 23/10/2024


a = int(input("Valor de a: "))
b = int(input("Valor de b: "))

while (a == b):
    print("OS VALORES DEVEM SER DIFERENTES.")
    a = int(input("Valor de a: "))
    b = int(input("Valor de b: "))

if (a > b):
    print(b , a)
    
else:
    print(a , b)
    


