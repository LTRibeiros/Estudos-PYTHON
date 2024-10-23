# Objetivo: Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

TP = int(input("Tempo de percurso: "))
VM  = float(input("Velocidade média: "))

QL = (TP * VM) / 12

print("Quantidade de litros gastos:" , QL)