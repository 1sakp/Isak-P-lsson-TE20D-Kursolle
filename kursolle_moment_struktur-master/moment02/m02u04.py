pennor = int(input("hur många pennor:   "))
pennorpris = int(input("Hur mycket kostar pennor:   "))
apple = int(input("hur många äpplen:   "))
applepris = int(input("hur mycket kostar äpplen:   "))
#med kommatecken:
print("Jag handlade ", pennor, " pennor för ", pennorpris, "kr och ",apple ," äpple för ",applepris ,"kr vilket totalt blev ",(pennor*pennorpris)+(apple*applepris) ,"kr.")
#med plustecken:
total = (pennor*pennorpris)+(apple*applepris)
print("Jag handlade "+str(pennor)+" pennor för "+str(pennorpris)+"kr och "+str(apple)+" äpple för "+str(applepris)+"kr vilket totalt blev "+str(total)+"kr.")
#med att bygga upp före utskrift:
s = ("Jag handlade "+str(pennor)+" pennor för "+str(pennorpris)+"kr och "+str(apple)+" äpple för "+str(applepris)+"kr vilket totalt blev "+str(total)+"kr.")
print(s)
#med öppen print utan att bryta rad:
print("Jag handlade", pennor, end="")
print(" pennor för ", pennorpris, "kr och ",apple ," äpple för ",applepris ,"kr vilket totalt blev ",(pennor*pennorpris)+(apple*applepris) ,"kr.")
#utskrift med format metoden:
print("Jag handlade {0} pennor för {1} kr och {2} äpple för {3} kr vilket totalt blev {4} kr.".format(pennor, pennorpris, apple, applepris, total))
#med fstring:
print(f"Jag handlade {pennor} pennor för {pennorpris} kr och {apple} äpple för {applepris} kr vilket totalt blev {total} kr.")