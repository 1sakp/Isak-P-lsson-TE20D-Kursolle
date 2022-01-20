from pickle import TRUE


again = 1
hojd = 1
num1 = 1
num2 = 1
x = 1
loop = True
def inmatning():
    global num1
    global num2
    global x
    num1 = int(input("Rektangle sida:   "))
    num2 = int(input("Rektangle sida:   "))
    x = 1
    hojdmatare()
    
def hojdmatare():
    global hojd
    global loop
    while loop == True:
        hojd = str(input("Hur hög?(1-10):     "))
        
        if "." or "," not in hojd:
            hojd = int(hojd)
            if hojd > 10:
                hojd = 10
                loop = False
                display()
            elif hojd < 0:
                hojd = 1
                loop = False
                display()
            else:
                loop = False
                display()
        else:
            print("please do integer:   ")
            loop = True
            
def display():
    global num1
    global num2
    global x
    global hojd
    print(f"area = {num1 * num2} ")

    if num1 == num2:
        print("den är kvadratisk")
    else:
        print("den är en rektangel")

    print("{0:^10s}|{1:^10s}".format("Höjd","volymen"))
    for i in range(1, hojd+1):
        print(f"{str(x):>10s}|{str(x*num1*num2):>10s}")
        x += 1
    koraigien()

def koraigien():
    fraga = input("Vill du köra en gång till?:  ")
    if "ja" in fraga.lower():
        inmatning()
    else:
        exit()
        
inmatning()