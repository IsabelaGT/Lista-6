"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 28/10/2023
Exercício: Programa 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela (utilizando lista).
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")


#Variáveis
notas = [ ]

#Lógica
for i in range(4):
    nota= float(input("Insira sua nota de 1 a 10: "))
    notas.append(nota)
soma = sum(notas)
media = soma/len(notas)

#Resultado
print("As suas notas foram:")
print(notas[0])
print(notas[1])
print(notas[2])
print(notas[3])
print("A sua média foi: ")
print(media)
