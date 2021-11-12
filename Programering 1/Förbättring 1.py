#Isak P, Elliot, Theo
#TE20D Best


list1 = []


antalelement = int(input("hut många element ska du ha i din lista: "))

for i in range(1, antalelement + 1):
    element = int(input("skriv in dina element är du snäll: "))
    list1.append(element)

list1.sort()
list1 = list(dict.fromkeys(list1))

print("det näst störst elementet är", list1[-2])
