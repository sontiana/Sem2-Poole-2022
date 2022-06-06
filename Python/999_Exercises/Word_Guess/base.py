import random
list_words =[]

with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)
    
answer = list_words[random.randrange(2315)]
a = 0
r = 6
for i in range(0,r) : 
    guess = input("Guess a 5 letter word: ")
    if answer == guess:
        print("You won!")
        break
    for word in list_words:
        if(guess == word1) :
            a = a+1
        
    if(a > 0):
        print("Wrong Answer ")
    else:
        print("Invalid word, guess again")
        r = r + 1 
    a = 0
print(answer)
    

f.close()
