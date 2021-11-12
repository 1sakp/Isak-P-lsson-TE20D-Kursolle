lista = [-2, 4 , 5, -4, 2, 8]

listapos = []
listaneg = []

for i in lista:
    if i > 0:
        listapos.append(i)
    else:
        listaneg.append(i)

print(listapos)
print(listaneg)