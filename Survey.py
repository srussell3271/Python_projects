import json

print("Welcome to the survey")

question = [
'What is your name?',
'How old are you?',
'When is your birhtday?',
'Where was you born?',
'How long do you spend on your phone everyday?',
'Are you an iphone user or andriod user?',
'What college do you want to go to?',
'What is your dream job?',
'Where do you see yourself in 10 years?',
'Do you have sibling?',
'What do you do for fun?',
'Do you live in a house or apt?',
'What was the last picture you took on your phone?',
'What is your middle name?',
'What did you have for dinner last night?'
'What school do you go to?',
'If you dont like your school what school would you go to?',
'If you had a superpower what would it be?',
'If you had one wish what would you wish for?'
]

surveys = []

while True:
    survey_response = {}
    i=0

    for q in question:
        response = input(q)
        survey_response[i] = response
        i +=1

    surveys.append(survey_response)

    # print(survey_response)
    print('Type end to see all your responses, if not press enter')
    answer = input()
    if answer == 'end':
        print(surveys)
        jsonToPython = json.dumps(survey_response)
        f = open("response.json", "w")
        f.write(jsonToPython)


        break
