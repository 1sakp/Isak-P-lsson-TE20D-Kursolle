import time as time
timme = time.localtime()

if int(timme.tm_hour) > 16:
    print("Skoldagen är slut")

if int(timme.tm_hour) <= 17:
    print("skoldagen fortsätter")