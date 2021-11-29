lon = int(input("Skriv brutto inkomst/månad i hela kr:    "))
arslon = lon*12

if arslon >= 19248:
    if arslon > 675700:
        print(print("månadslön: {:.0f}    (årslön: {:.0f})\nkomunalskatt: {:.0f}\nlandtingsskatt: {:.0f}\nStadsskatt: {:.0f}\nKvar efter skatt: {:.0f}".format(lon, 
        arslon, (lon/100)*21.36, (lon/100)*11.48, (lon/100)*25, lon-((((((lon/100)*11.48))+((lon/100)*21.36))+(lon/100)*20))+(lon/100)*5)))
        
    elif arslon > 468700:
        print(print("månadslön: {:.0f}    (årslön: {:.0f})\nkomunalskatt: {:.0f}\nlandtingsskatt: {:.0f}\nStadsskatt: {:.0f}\nKvar efter skatt: {:.0f}".format(lon, 
        arslon, (lon/100)*21.36, (lon/100)*11.48, (lon/100)*20, lon-(((lon/100)*11.48)+((lon/100)*21.36)+(lon/100)*20))))
        
    else:
        print("månadslön: {:.0f}    (årslön: {:.0f})\nkomunalskatt: {:.0f}\nlandtingsskatt: {:.0f}\nKvar efter skatt: {:.0f}".format(lon, 
        arslon, (lon/100)*21.36, (lon/100)*11.48, lon-(((lon/100)*11.48)+((lon/100)*21.36))))

if arslon < 19247:
    print("månadslön: {:.0f}    (årslön: {:.0f})\nKvar efter skatt: {:.0f}\nEftersom du känar mindre en brytpungkten så betalar du ingen skatt".format(
        lon, arslon, lon))