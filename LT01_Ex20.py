# Objetivo: Receba 4 notas bimestrais de um aluno. 
# Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#a.	Se a média for >= 6,0 exibir “APROVADO”;
#b.	Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
#c.	Se a média for < 3,0 exibir “RETIDO”.

# Programador: Gabriel Ribeiro
# Data de Elaboração: 23/10/2024

N1 = float(input("Valor da 1° nota: "))
N2 = float(input("Valor da 2° nota: "))
N3 = float(input("Valor da 3° nota: "))
N4 = float(input("Valor da 4° nota: "))


media = (N1 + N2 + N3 + N4) / 4

if media >= 6 and media <= 10:
    print("APROVADO. ", media)

elif media >=3 and media < 6:
    print("EXAME. ", media)

elif media < 3 and media > 0:
    print("RETIDO. ", media)    

else:
    print("Valor inválido")    
    
