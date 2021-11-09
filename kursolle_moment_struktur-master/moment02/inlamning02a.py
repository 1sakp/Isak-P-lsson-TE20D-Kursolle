#Funktion: att räkna ut area, diameter och omkrets på den radie som andvändaren skriver.

#Definerar variabler aka pi och radie. Valde att ha en float istället för en int för att det blir mer precist
pi = 3.14
radie = float(input("Skriv radie med decimaler aka med pungkt: "))

#Här räknar jag ut och printar dem olika delarna. Jag andvänder \u00b2 på arean så att det ska se fint ut. 
#Samtidigt så andvänder jag {:.2f} för att få 2 decimaler istälet för fler eller färre.
#Jag gör uträkningarna i format för att det minskar antalet rader jämfört med att definera nya variablar och sedan printa dem.
print("radie: {:.2f}cm".format(radie))
print("diameter: {:.2f}cm".format(radie*2))
print("omkrets: {:.2f}cm".format(((pi+pi)*radie)))
print("area: {:.2f}cm\u00b2".format(((radie*radie)*pi)))
