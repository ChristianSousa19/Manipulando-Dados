import random
p1=str(input("digite o nome do primeiro aluno"))
p2=str(input("digite o nome do segundo aluno"))
p3=str(input("digite o nome do terceiro aluno"))
lista=[p1,p2,p3,]
escolhido=random.choice(lista)
print("o aluno escolhido foi {} ".format(escolhido))
