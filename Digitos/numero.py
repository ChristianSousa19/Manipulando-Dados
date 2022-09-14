num=int(input("Digite um numero"))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print("Analisando o numero {}".format(num))
print("Sua unidade é {}".format(u))
print("Sua dezena é  {}".format(d))
print("sua centena é {}".format(c))
print("seu milhar e  {}".format(m))