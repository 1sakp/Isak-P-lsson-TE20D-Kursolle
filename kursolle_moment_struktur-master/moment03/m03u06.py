import time as time
timme = time.localtime()

if int(timme.tm_hour) >= 17 and int(timme.tm_hour) < 23:
    print("Skoldagen är slut")

if int(timme.tm_hour) <= 16 and int(timme.tm_hour) >= 8:
    print("skoldagen fortsätter")

if int(timme.tm_hour) >= 0 and int(timme.tm_hour) <= 7:
    print("skoldagen har inte börjat")

#import time
#set variable

#om timmar är mellan 17 och 23
#   skriv skoldagen är slut

#om timmar är mellan 16 och 8
#   skriv skoldagen forsätter

#om timmar är mellan 0 och 7
#   skriv skoldagen har inte börjat