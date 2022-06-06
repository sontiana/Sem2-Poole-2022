name1 = "Jun's Farm Fresh Produce"
menu1 = "Organic Bananas: 1lb for 0.50$"
menu2 = "Ripe Strawberries: 1 carton for 4.50$"
menu3 = "Large Eggplants: you can have them they taste bad"

print(name1)
print(menu1)
print(menu2)
print(menu3)

ban1 = int(input("How many lbs of bananas would you like?  "))
ban2 = int(input("How many cartons of strawberries would you like?  "))
ban3 = int(input("How many eggplants would you like?  "))

num1 = ban1*0.5
num2 = ban2*4.5
num3 = ban3*0
sum1 = num1+num2+num3

print("Thanks for shopping with us")
print("Your total is " + str(sum1))
print("You paid " + str(num1) + " for " + str(ban1) + " lbs of bananas")
print("You paid " + str(num2) + " for " + str(ban2) + " cartons of strawberries")
print("You paid " + str(num3) + " for " + str(ban3) + " large eggplants")