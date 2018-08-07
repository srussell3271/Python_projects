# --- Define your function
def process_input(input):
    greetings = ["hey" , "howdy" , "hi" , "hello" , "hola" , "wassup"];
    farewell = ["Goodbye" , "bye" , "adios", "see ya" , "peace" , "later"];
    poems = ["tell me a poem", "poetry", "say something poetic"];
    today = ["what is today date?" , "date", "today"];
    life = ["what is life?", "why do i exist", "life"];
    divide = ["0/0", "zero divided by zero", "show me error"];

    if is_valid_input(input, greetings):
        greeting()
    elif input == "hello":
        greeting()
    elif is_valid_input(input, poems):
        poem()
    elif is_valid_input(input, today):
        date()
    elif input == "how old are you?":
        age()
    elif is_valid_input(input, life):
        lifes()
    elif is_valid_input(input, divide):
        divided()
    elif input == "tell me about yourself":
        yourself()
    elif input == "take me home":
        home()
    elif is_valid_input(input, farewell):
        farewells()
    else:
        default()

def introduction():
    print("Hi! My name is Shaybot ")

def greeting():
    print("Hi, how are you?")

def farewells():
    print("Later~")
    quit()

def default():
    print("Anything else?")

def poem():
    print('''
        Everything you do is with a purpose
        It may not be for the best reasons
        So don't be nervous
        The best things has an appearance

        Keep doing what you do
        Don't think about pressing undo
        You tried your best
        Thank you now, go rest
        ''')

def date():
    print("Today is I don't know, 2018")

def age():
    print('''
        Isn't it rude to ask how old am I?
        What if I said you looked like you are
        102 years-old? Now stop asking
        ''')

def lifes():
    print('''
        You been in this world for a few years!
        Why are you asking me what is life?
        ''')
def divided():
    print('''
    ErRoR 100101101010101010101010101101010101
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    101010101011101010110101010101010101010101
    010111010110101010110101010101101010101010
    ''')

def yourself():
    print('''
        Mine your damn business!
        So damn disrespectful
        If you ask questions like that you will be in jail
        I dare you to ask a cop that
        You know how suspicious you sound?
        ''')

def home():
    print("Get your lazy ass up and walk home then -_-")

def is_valid_input(user_input, valid_responses):
    if user_input in valid_responses:
        return True
    else:
        return False

# --- Put your main program below! ---
def main():
    introduction()
    while True:
        answer = input("(Say something) ")
        process_input(answer);

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main();
