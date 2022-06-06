sen1 = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
num1 = 0 

for i in range(0, len(sen1)):
    if sen1[i:i+5] == "whale":
        num1 = num1 + 1
    
print(num1)

