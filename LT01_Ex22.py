# Objetivo: Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor 
# não necessariamente em ordem. 
# Mostre os 4 números em ordem crescente
# Programador: Gabriel Ribeiro
# Data de Elaboração: 23/10/2024

VT = []
i = 0
j = (i + 1) 

for i in range(0, 3):
    VT.append(int(input("Insira um valor: ")))
N4 = int(input("Insira o 4° número: "))
VT.append(N4)
for i in range(0, 4):
    for j in range((i + 1), 4):
     if VT[i] > VT[j]:
        aux = VT[j]
        VT[j] = VT[i]
        VT[i] = aux

for i in range(0, 4):
    print(VT[i])

   


      
    


