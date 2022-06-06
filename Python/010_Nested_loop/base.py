char1 = str(input("Please input a character "))
char2 = int(input("How high do you want your box to be? "))
char3 = int(input("How wide do you want your box to be? "))
for i in range(0, char2):
    for x in range(0, char3):
        print(char1, end="")     
    print()