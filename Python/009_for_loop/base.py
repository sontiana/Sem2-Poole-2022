leng1 = int(input("How long do you want the line "))
leng2 = str(input("horizontal or vertical "))
if leng2 == "horizontal":
    for x in range(0, leng1):
        print("o", end="")
elif leng2 == "vertical":
    for x in range(0, leng1):
        print("o")