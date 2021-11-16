import time as time
timme = time.localtime()

if int(timme.tm_hour) >= 17 and int(timme.tm_hour) < 23:
    print("Skoldagen är slut")

if int(timme.tm_hour) <= 16 and int(timme.tm_hour) >= 8:
    print("skoldagen fortsätter")

if int(timme.tm_hour) >= 0 and int(timme.tm_hour) <= 7:
    print("skoldagen har inte börjat")