again = 1
while again == 1:
    num1 = int(input("Rektangle sida:   "))
    num2 = int(input("Rektangle sida:   "))
    x = 1
    loop = True
    
    while loop == True:
        hojd = str(input("Hur hög?:     "))
        
        if "." or "," not in hojd:
            hojd = int(hojd)
            if hojd > 10:
                hojd = 10
                loop = False
            elif hojd < 0:
                hojd = 1
                loop = False
            else:
                loop = False
        else:
            print("please do integer:   ")
            loop = True
            

    print(f"area = {num1 * num2} ")

    if num1 == num2:
        print("den är kvadratisk")
    else:
        print("den är en rektangel")

    print("{0:^10s}|{1:^10s}".format("Höjd","volymen"))
    for i in range(1, hojd+1):
        print(f"{str(x):>10s}|{str(x*num1*num2):>10s}")
        x += 1
        
    fraga = input("Vill du köra en gång till?:  ")
    if "ja" in fraga.lower():
        again = 1
    else:
        again = 0