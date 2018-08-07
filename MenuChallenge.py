imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Chicken" , "Crabs" , "Lamb" , "Lobester" , "Steak" , "Goat"]
bList = ["Rice" , "Macaroni" , "Potatoes" , "Fries"]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)
aRandomIndex2 = randint(0, len(bList)-1)

print(aList[aRandomIndex] + " " + bList[aRandomIndex2])
5
