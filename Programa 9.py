"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 02/11/2023
Exercício: Programa 9 -  Faça um Programa que leia uma lista A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos da lista.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
A = [ ]
soma_quadrado = 0

#Lógica
for i in range(10):
    num = int(input("Insira um número inteiro: "))
    soma_quadrado += num**2
    A.append(soma_quadrado)

print(A[9]) #Resultado



