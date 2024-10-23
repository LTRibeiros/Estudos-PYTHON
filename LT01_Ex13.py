# Objetivo: Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

kg = int(input("Quantidade de alimento em kg: "))

dias = (kg * 1000) / 50

print("O alimento durará" , dias , "dias.")
