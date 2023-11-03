"""
Nome do desenvolvedor: Isabela Garcia Tissianel
Data: 02/11/2023
Exercício: Programa 8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação em sua respectiva lista. Imprima a idade e a altura na ordem inversa a ordem lida.


"""
#Front-end
print("--------------------------------------------------")
print("----------------------Listas----------------------")
print("--------------------------------------------------")

#Variáveis
idades = [ ]
alturas = [ ]
i = 0

#Lógica
for i in range(5):
    print("\nPessoa", i + 1)
    idade = int(input("Insira a sua idade em anos: "))
    altura = float(input("Insira a sua altura em metros: "))
    idades.append(idade)
    alturas.append(altura)

#Resultado
for i in range(5):    
    print("Idade: ",idades[-i-1] , end = " " )
    print("Altura: ",alturas[-i-1] )
