foods = ["Chicken Nuggets" , "Fried Chicken" , "Baked Chicken" , "Jerk Chicken" , "Grill Chicken" , "Crispy Chicken"]
#weights = [153.4, 81.2, 1293.4, 432.6] #random_data = ["Ada Lovelace", 8, 10.2]
print(foods)
print(len(foods))
#
i=0
while i< len(foods):
    print(foods[i])
    i+=1

# # print("Shannon" in friends)
# # print("Giselle" in friends)
# for name in friends:
#     print(name)

anExample = "Bread"
print(len(anExample))
# Output: 4
print("B" in anExample)
# Output: True
print(anExample[0])
# Output: a
print(anExample[0] + anExample[1])
print(anExample[0] + anExample[1] + anExample[2])
print(anExample[0] + anExample[1] + anExample[2] + anExample[3])
print(anExample[0] + anExample[1] + anExample[2] + anExample[3] + anExample[4])
#Output: ad
for letter in anExample:
    print(letter)
