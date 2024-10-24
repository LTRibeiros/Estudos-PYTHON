# Objetivo: Receba 2 valores reais. Calcule e mostre o maior deles.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 23/10/2024

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))

if a > b:
    print("Maior valor entre a e b:" , a)

elif b > a:
    print("Maior valor entre a e b:" , b)

else: 
    print("Os valores são iguais.")


