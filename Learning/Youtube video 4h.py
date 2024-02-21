def class1(Elegible):
# write class1 (True/False)
# Variables, if else (sum, round, str)
    Account_name = "Borgo"
    Factor = -5.65
    Account_number = 75
    Position = Account_number + Factor

    print("1st class")
    print("Welcome " + Account_name + ". Your current position is " + str(round(Position)))
    if Elegible:
        print("and you are elegible to enter in the site!")
    else:
        print("Sorry, you're not elegible to enter in the site yet.")
    print("________________")

def class2():
# try except, input, list, tuples, function, multiplication
    print("2nd class")
    try:
        print ("How much can you squat?")
        num1 = input("enter your weight:")
        num2 = input("how much you squat:")
        result = float(num1) + float(num2)
        print("The total weight you can squat is: " + str(result) + "Kg")
    except ValueError:
        print ("Sorry, only round numbers are accepted.")

    list = [1, 3,"giowi"]
    list_tuples = ("giogio", "swaggo", "mekko")
    list.insert(1, 2)
    list.extend(list_tuples)
    print (list)

    def function(name, age):
        print("Your name is " + name + ", and you're " + str(age))

    function ("Nicolò", 23)

    def function2 (num):
        return num*num*num

    cube = function2(3)
    print (cube)




def class3():
# dictionary, .get, while loop,
    print ("3rd class")
    dizionario = {
        "ita" : "Via pianette 16/c",
        "esp" : "Carrer pla de fornells 39, 2 2",
        "nl" : "Mozartlaan 216/a",
    }
    print("In italia vivevi in " + dizionario["ita"])

    print(dizionario.get ("fr", "You didn't lived there yet"))

    secret_word = "weed"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    print ("What is the flower that all the teenagers love?")

    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input ("Your answer: ")
            guess= guess.lower()
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print ("You've run out of guesses!")
    else:
        print ("You won! Here's a joint for you <3")

def class4():
    #for loop, return, range

    #oppure posso fare range(3) [dunque 0,1,2] e printare friends[0], friends[1], ecc.. individualmente
    #    for index in range(len(friends)):
    #        print (friends[index])
    friends = ["gio", "lukas", "hans"]
    for friend in friends:
        print (friend)

    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                transla2tion = translation + "g"
            else:
                translation = translation + letter
        return translation

    print(translate(input("Enter a Phrase:")))

class4() #need to learn "with" function