num1 = int(input("Rectangle side:   "))
num2 = int(input("Rectangle side:   "))
x = 1

print(f"area = {num1 * num2} ")

if num1 == num2:
    print("is kvadrat")
else:
    print("is rektangel")

print("{0:^10s}|{1:^10s}".format("Höjd","volymen"))
for i in range(1, 11):
    print(f"{str(x):>10s}|{str(x*num1*num2):>10s}")
    x += 1