"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 
Exercício: Programa 2 - Faça um Programa que leia um lista de 10 números reais e mostre-os na ordem inversa.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
nums = [ ]

#Lógica
for i in range(10):
    num = float(input("Insira um número real: "))
    nums.append(num)
for i in range(10):    
    print(nums[-i-1] )

#Resultado

