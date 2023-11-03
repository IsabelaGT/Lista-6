"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 02/11/2023
Exercício: Programa 7 - Faça um Programa que leia uma lista de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
lista = [ ]

#Lógica
for i in range(5):
    num = float(input("Insira um número: "))
    lista.append(num)
soma  = lista[0]+lista[1]+lista[2]+lista[3]+lista[4]
multi = lista[0]*lista[1]*lista[2]*lista[3]*lista[4]

print("\n", lista) #Resultado

print(" Soma: ", soma) #Resultado

print(" Multiplicação: ", multi)#Resultado


