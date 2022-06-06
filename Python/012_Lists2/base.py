num1 = int(input("How many numbers would you like? "))
thislist = []
import random
for i in range(0,num1):
    x = random.randrange(0,10)
    thislist.append(x)
print(thislist)
