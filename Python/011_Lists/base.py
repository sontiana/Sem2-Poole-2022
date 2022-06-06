print("Random Joke Generator")
thislist = ["Your Mother", "Your Mommy", "Deez Nuts", "I can't make good jokes", "You"]
import random
x = random.randrange(0,5)
print(thislist[x])

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()



example1.py
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
 
>>> min( nums )
 
-4    #Min value in array

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)
  
# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
  
# Printing average of the list
print("Average of the list =", round(average, 2))