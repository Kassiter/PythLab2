import math, random
handle = open("x.txt", "w")
i=0
j=input();
while i<=j:
    x = random.uniform(-15, 20)
    print(x)
    handle.write(x)
handle.close()
i=0;
while i<=j:
    if x==4:
        print(math.sqrt(x)+4)
    elif (x>-10) & (x<=16):
        print(x**2)
    elif (x<-8):
        print(x**-1)
