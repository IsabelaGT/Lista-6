"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 28/10/2023
Exercício: Programa 5 - Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números pares no vetor PAR e os 
números IMPARES no vetor impar. Imprima as três listas.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
nums = []
par = []
impar = []

#Lógica
for i in range(20):
    num = int(input("Insira um número: "))
    nums.append(num)
    if num % 2 != 0:
        impar.append(num)
    else:
        par.append(num)

#Resultado
print(nums)
print(par)
print(impar)
