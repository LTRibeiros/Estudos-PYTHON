# Objetivo: Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

deposito = float(input("Valor do depósito: "))

aplicacao = deposito * (1.3 / 100)

deposito_F = deposito + aplicacao

print("Valor do depósito após 1 mês de aplicação:" , deposito_F)
