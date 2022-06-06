sym = str(input("Pick a symbol"))
wid = int(input("What is the width"))
hei = int(input("What is the height"))
for i in range(0, hei):
    for x in range(0, wid):
        print(sym, end="")     
    print()