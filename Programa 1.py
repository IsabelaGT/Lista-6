"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 28/10/2023
Exercício: Programa 1 - Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
lista = [1,2,3,4,5]

#Lógica e Resultado
print(lista) #Aqui eu não entendi se devo pedir ao usuário para inserir ou não um número, então vou fazer dos dois modos.


#Variáveis
nums = [ ]

#Lógica
for i in range(5):
    num = int(input("Insira um número inteiro: "))
    nums.append(num)
print(nums)