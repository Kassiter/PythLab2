import math, random


def func(x):
    if x == 4:
        print(math.sqrt(x) + 4)
    elif (x > -10) & (x <= 16):
        print(x ** 2)
    elif (x < -8):
        print(x ** -1)
    return


handle = open("x.txt", "w")
i = 0
j = input("Enter amount of x");
j = int(j)
while i <= j:
    x = random.uniform(-15, 20)
    func(x)
    print("x: " + str(x))
    handle.write(str(x))
    i = i + 1
handle.close()




