frase=str(input("digite uma frase").upper().strip())
print("A letra C aparece {} na frase".format(frase.count("C")))
print(" A  primeira letra c apareceu na posição {}".format(frase.find("C")+1))
print(" a letra c aparece pela ultima vez na posição {}".format(frase.rfind("C")+1))