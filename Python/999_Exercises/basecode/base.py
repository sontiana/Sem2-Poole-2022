num1 = int(input("How many items are you purchasing? "))

total = 0
for i in range(0,num1):
    item1 = str(input("What item are you purchasing? "))
    pric1 = float(input("How much is the item? "))
    print("You purchased " + item1)
    total = total + pric1
    
print("Your total is: " + str(total))