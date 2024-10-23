# Objetivo: Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

a = int(input("Valor do 1° cateto: "))
b = int(input("Valor do 2° cateto: "))

c = ((a ** 2 + b ** 2) ** 0.5)

print("Valor da hipotenusa:" , c)
