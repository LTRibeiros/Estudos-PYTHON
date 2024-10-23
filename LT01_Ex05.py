# Objetivo: Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

A = float(input("Valor de A: "))
B = float(input("Valor de B: "))
C = float(input("Valor de C: "))
delta = (B ** 2) - (4 * A * C)

print("O valor de delta é de: ", delta)

R1 = (-B + (delta ** 0.5)) / (2 * A)
R2 = (-B - (delta ** 0.5)) / (2 * A)

print("O valor da raiz 1 é de:", R1)
print("O valor da raiz 2 é de:", R2)