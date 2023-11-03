"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 02/11/2023
Exercício: Programa 6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média 
maior ou igual a 7.0.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
alunos = []
qt_alunos = 0
i = 0

#Lógica
for i in range(10):
    print("\nNotas do aluno", i + 1)
    total = 0
    for j in range(4):
        nota = float(input("Insira a nota do aluno de 1 a 10: "))
        total += nota 
    media = total/4
    alunos.append(media)
    if media >= 7:
        qt_alunos += 1

print(f"\nA quntidade de alunos com média maior ou igual a 7 são: {qt_alunos} alunos") #Resultado



