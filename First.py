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
handle.write("")
handle.close()
f = open('x.txt')
arr=[]
i=0
for lines in f.readlines():
    items = lines.strip("()\n").split(",")
    arr += items
y = open("y.txt", "w")
i=0
yarr =arr
print("arrlen: ")
print(arr.__len__())
while i<arr.__len__():
    print("entered func")
    if float(arr[i]) == 4:
        yarr[i]=(str(math.sqrt(float(arr[i])) + 4))
    elif (float(arr[i]) > -10) & (float(arr[i]) <= 16):
        yarr[i] =(str(float(arr[i]) ** 2))
    elif (float(arr[i]) < -8):
        yarr[i] =(str(float(arr[i]) ** -1))
    print("Written")
    i=i+1
i=0
while i<yarr.__len__():
    y.write(yarr[i]+"\n")
    i=i+1
y.close()





