# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.
sek1 = float(input("Hur många SEK vill du växla till dollar: "))#fixade citat tecken och variablen 1sek till sek1 och så att det blir en float eftersom det är ett nummer
exchange_rate = 8.82 #jag fixade var = tecknet skulle sitta och var ett + skulle sitta, fixade också positionen så variablerna fungerar och en pungkt istället för ett kommatecken så att det fungerar
dollar = sek1 / exchange_rate #fixade positionen och variablen sek1
print("Detta är ett program där vi kan växla mellan SEK & dollar") #hadde inga citat tecken
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek1, dollar))#fixade igien variablen sek1 och ett till parantes täcken i slutet