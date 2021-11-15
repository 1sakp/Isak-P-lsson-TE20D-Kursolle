alder = (input("hur gammal är du:    "))
alder = alder.strip()
namn = input("Vad är ditt namn:     ")
namn = namn.strip()

if int(alder) >= 18:
    myndig = "myndig"
else:
    myndig = "inte myndig"

print("{} är {}år gammal och är därför {}. Den första bokstaven är {}".format(namn, alder, myndig, namn[0]))