# Objetivo: Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
# Programador: Gabriel Ribeiro
# Data de Elaboração: 22/10/2024

# sinceramente eu adoro fazer isso, já me ajudou muito

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

aux = y
y = x
x = aux

print("Valor de x:" , x)
print("Valor de y:" , y)