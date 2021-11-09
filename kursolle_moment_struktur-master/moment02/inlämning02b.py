#Uppgift: att göra om sekunder till minuter och timmar och sedan printa ut dem

#Sätter variabler
sec = int(input("Skriv sekunder: "))
tim = 0
min = 0

#Här räknar jag ut från sekunder till minuter och från minuter till timmar genom att andvända logiska "gates" där 
#den slår över ett nummer om det numret innan är över en viss gräns.
while 1 == 1:
    if sec >= 60:
        min+=1
        sec-=60
    if min >= 60:
        tim+=1
        min-=60
    
    #För att printa tiden och sedan stänga ner programmet. Detta sker när sec(sekunder) är mindre än 60,
    #vilket ändå inte skulle fortsatt då den inte räknar mer när sec är mindre en 60.
    if sec < 60:
        print("{}sec {}min {}tim".format(sec, min, tim))
        exit()
