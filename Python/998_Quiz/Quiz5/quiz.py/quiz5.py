
# Create a program that takes in two inputs:
# 1. A sentence from the user saying their favorite number. Ex: "My favorite number is 42"
# 2. Ask the user to input their age. 

# 3. Take the first sentence (it can be the same every time) and use slicing to cut out the number. 
# 4. Multiply their favorite number against their age and print it out.

favNum1 = input("What is your favorite number? (i love 5) ")
birNum = int(input("How old are you? "))
favNum2 = favNum1[7]
prod1 = int(favNum2)*birNum
print("So you like the number " + favNum2 + " and you are " + str(birNum) + " years old")
print("The product of those two numbers is " + str(prod1))
     
