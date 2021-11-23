lon = int(input("Skriv brutto inkomst/månad i hela kr:    "))

print("månadslön: {:.0f}\nkomunalskatt: {:.0f}\nlandtingsskatt: {:.0f}\nKvar efter skatt: {:.0f}".format(lon, 
(lon/100)*21.36, (lon/100)*11.48, lon-(((lon/100)*11.48)+((lon/100)*21.36))))