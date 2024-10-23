# Objetivo: Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. 
# Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). 
# A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

QH = float(input("Quantidade de horas trabalhadas: "))
VP = float(input("Valor pago por hora: "))
PD = float(input("Percentual de desconto: "))
ND = int(input("Numero de Descendentes: "))

desconto = PD / 100
salario = QH * VP
salario_L = salario - (salario * desconto) + (ND * 100)

print("Valor do salário liquído:" , salario_L)
