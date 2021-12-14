num1 = int(input("Rektangle sida:   "))
num2 = int(input("Rektangle sida:   "))
x = 1

print(f"area = {num1 * num2} ")

if num1 == num2:
    print("den är kvadratisk")
else:
    print("den är en rektangel")

print("{0:^10s}|{1:^10s}".format("Höjd","volymen"))
for i in range(1, 11):
    print(f"{str(x):>10s}|{str(x*num1*num2):>10s}")
    x += 1