num1 = int(input("Please input an integer "))
char1 = str(input("What operation (addition, subtraction, multiplication, division) "))
num2 = int(input("Please input another integer "))
if char1 == "addition":
    ans1 = num1+num2 
    print(str(ans1))
elif char1 == "subtraction":
    ans1 = num1-num2
    print(str(ans1))
elif char1 == "multiplication":
    ans1 = num1*num2
    print(str(ans1))
elif char1 == "division":
    ans1 = num1/num2
    print(str(ans1))
else:
    print("You did n0t select an operation listed above in the parentheses. Please type it exactly as you see it ")