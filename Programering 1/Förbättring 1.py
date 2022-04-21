# importerar time modulen
import time

# definerar funktion alarmklocka
def alarmklocka ():
    t = int(input("Enter the time in seconds: "))
    t_temp = t
    while t >= 0:
        mins, sek = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, sek)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    name = input("Var snäll och skriv ditt namn:    ")
    with open("logg.txt", "a+") as file: 
        file.write(f"{name} {t_temp} sekunder\n")
    file.close()
    
    with open("logg.txt", "r") as file_read:
        line = file_read.readline()
        while line:
            line = file_read.readline()
            print(line)
    file_read.close

        
        
        
  
  
# kallar på funktion alarmklocka
alarmklocka()