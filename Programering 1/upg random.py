import math as ma
def bucket():
    print("It's a bucket made of metal")
    x = input("Do you want to look inside: yes/no:  ")
    if x == "yes":
        print("There is whater inside, you return to the center of the room")
    else:
        print("you walk back to the center of the room")

def cabinet():
    x = input("it's a cabinet and its locked, it looks breakeble, do you want to break it?: yes/no: ")
    if x == "yes":
        print("you break your toe, you return to the center of the room")
    else:
        print("you walk back to the center of the room")

def miniraknare():
    l = int(1)
    while l == int(1):
        x = int(input("Do you want to use the calculator? 1=yes 2=no :  "))
        if x == 1:
            y = int(input("pythagaros=1 calculate-energy=2"))
            if y == 1:
                a = int(input("first side:  "))
                b = int(input("second side:  "))
                c = a**b
                c = ma.sqrt(c)
                print(c)
            elif y == 2:
                a = int(input("mass:  "))
                b = int(input("heigt:  "))
                d = int(input("time:    "))
                c = (a*b*9.82)/d
                print(c)
            else:
                print("error you put in the wrong number")
        else:
            print("You go to the center of the room")
            break
        y = input("do you want to continue to use the miniraknare: y/n: ")
        if y == "y":
            l=1
        else:
            l=0
        

        

while 1==1:
    fraga = int(input("You are in the center of the room. What do you want to look at: 1-bucket 2-cabinet 3-miniraknare"))
    if fraga == 3:
        miniraknare()
    elif fraga == 2:
        cabinet()
    else:
        bucket()



def matte(x, y):
    x+=y
    print(x)

matte(5, 8)