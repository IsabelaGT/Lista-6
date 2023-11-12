"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 28/10/2023
Exercício: Programa 4 - Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
letras = [ ]
tam = 0

#Lógica
for i in range(10):
    letra = str(input("Insira uma letra: "))

    if not(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        letras.append(letra)
        tam = tam + 1

#Resultado
print(letras)
print("Quantidade de consoantes: ", tam)        

