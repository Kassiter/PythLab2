import math, random
import matplotlib.pyplot as plt

handle = open("x.txt", "w")
y = open("y.txt", "w")

def toFile(name,k):
    f = open(name, "w")
    i1=0
    while i1 <= k:
        x = random.uniform(-15, 20)
        f.write(str(x) + "\n")
        i1 = i1 + 1
    f.write("")
    f.close()


def fromFile(name):
    output=[]
    ff = open(name, "r+")
    for lines in ff.readlines():
        items = lines.strip("()\n").split(",")
        output += items
    ff.close()
    return output


def func(x1): #Тут вписываем свою функцию
    if x1 == 4:
        return (math.sqrt(float(x1)) + 4)
    elif (float(x1) > -10) & (float(x1) <= 16):
        return (float(x1) ** 2)
    elif (float(x1) < -8):
        return (float(x1) ** -1)
    return


def trunc(arr): #переопределяем trunc (отрезание чисел после запятой)
    l=0
    while l<arr.__len__():
        arr[l]=math.trunc(float(arr[l])) #Используем уже существующую ф-цию "trunc", принимающую значение float
        print(arr[l])
        l=l+1
    return arr

i = 0
j = input("Enter amount of x");
j = int(j)
toFile("x.txt",j)

arr=[]
i=0
arr=fromFile("x.txt")
i=0
yarr =arr
while i<arr.__len__():
    yarr[i]=func(arr[i])
    i=i+1
i=0
while i<yarr.__len__():
    y.write(str(yarr[i])+"\n")
    i=i+1
y.close()

Yaxis=trunc(fromFile("y.txt")) #вызов переопределенной нами функции trunc
Xaxis=trunc(fromFile("x.txt"))
plt.plot(Xaxis,Yaxis) #строим график по целым числам
plt.ylabel('ТУТ ПИШЕМ СВОЮ ФУНКЦИЮ')
plt.show()



