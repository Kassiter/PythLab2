import math, random


def func(x1):
    if x == 4:
        return (math.sqrt(x) + 4)
    elif (x > -10) & (x <= 16):
        return (x ** 2)
    elif (x < -8):
        return (x ** -1)
    return


handle = open("x.txt", "w")
i = 0
j = input("Enter amount of x");
j = int(j)
while i <= j:
    x = random.uniform(-15, 20)
    print(func(x))
    print("x: " + str(x))
    handle.write(str(x)+"\n")
    i = i + 1
handle.close()
f = open('x.txt')
for lines in f.readlines():
    arr = lines
y = open("y.txt", "w")
while i<=j:

    if int(arr[i]) == 4:
        y.write(math.sqrt(int(arr[i])) + 4)
        i=i+1
        continue
    elif (int(arr[i]) > -10) & (int(arr[i]) <= 16):
        y.write(int(arr[i]) ** 2)
        i=i+1
        continue
    elif (int(arr[i]) < -8):
        y.write(int(arr[i]) ** -1)
        i=i+1
        print()
        continue
    print("Written")
y.close()





