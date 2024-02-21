# Final Exercise (too high, too low)
import random
print ("random number from 1 to 100")
h_list = list(range(1, 101))
number = random.choice(h_list)
attempts = int(input("5 or 10 attempts?:"))
playing = True
def check():
    global attempts
    if guess > number:
        print ("too high")
    elif guess < number:
        print ("too low")
    elif guess == number:
        print (f"you won. The number was {number}")
        return False
    return True


while playing:
    guess = int(input("make a guess:"))
    playing = check()
    attempts -= 1
    if attempts == 0:
        print("you lost, 0 attempts left.")
        playing = False









