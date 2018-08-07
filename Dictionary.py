# # Declare Dictionary
# person = dict()
# # Assign values
# person['Shannon'] = 'Shannon is 15 years old'
# person['Giselle'] = 'Giselle is 16 years old'
# person['Jimmy Fallon'] = 'Jimmy Fallon is 43 years old'
# person['Jamie Dornan'] = 'Jamie Dornan is 36 years old. AND MY HUSBAND!'
# person['Tania'] = 'Tania is 16 years old'
# person['Kayla Ramos'] = 'Kayla R. is 15 years old'
#
# print(person['Jamie Dornan'])
# print(person['Shannon'])

name_age = {
    "Shannon":15,
    "Tania":16,
    "Kayla.R":15
    }
    # print(name_ages) #Show how above looks like

for key, val in name_age.items():
    # print(key, " is",val, " years old")
# Loops the above text to read as a sentence

# How to find average
    age_sum = 0
    for key, val in name_age.items():
        age_sum += val

    average = age_sum / len(name_age)
    print(average)
