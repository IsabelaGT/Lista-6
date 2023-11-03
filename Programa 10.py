"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 02/11/2023
Exercício: Programa 10 - Faça um Programa que leia duas listas com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados de duas 
outras listas.
"""

#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
a = [ ]
b = [ ]
c = [ ]

#Lógica
print("Na lista A")
for i in range(10):
    a.append(
    int(input("Insira um número: "))
    )
print("\nNa lista B")
for i in range(10):
    b.append(
    int(input("Insira um número: "))
    )

for i in range(10):
    c.append(a[i])
    c.append(b[i])
#Resultado
print("\nElementos da lista A", a)
print("\nElementos da lista B", b)
print("\nElementos intercalados", c)
