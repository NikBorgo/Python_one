# 1st exercise (import and random)
import random
result = random.randint(0, 1)
if result == 0:
    print("Heads")
else:
    print("Tails")

# 2nd exercise (lists)
list = ["Gio", "Nico", "Antonella"]
import random
n_people = len(list)
n_payer = random.randint(0, n_people - 1) #cause lenght starts from 1
who_pays = list[n_payer]
print(f"{who_pays} goes to buy xurros!")

# 3rd exercise (nested lists)
list_1 = ["□", "□", "□"]
list_2 = ["□", "□", "□"]
list_3 = ["□", "□", "□"]
map = [list_1, list_2, list_3]
print(f"{list_1}\n{list_2}\n{list_3}")

x_coordinate = input("Set a coordinate where the treasure is: ") #x= B3
zero_index = x_coordinate[0].lower()
letters = ["a", "b", "c"]
letter_index = letters.index(zero_index)
number_index = int(x_coordinate[1])-1
map[number_index][letter_index] = "X"
print(f"{list_1}\n{list_2}\n{list_3}")

# last exercise: Rock Paper and Scissors
import random
me = int(input("What do you choose? Rock(0), Paper(1), Scissors(2): "))
rock ="""
 # Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper ="""
 # Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
 # Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list = [rock, paper, scissors]
me = int(me)
pc = random.randint(0, 2)

while me >= 3 or me < 0:
    print ("Invalid number!")
    me = int(input("What do you choose? Rock(0), Paper(1), Scissors(2): "))
else:
    print(list[me])
    print(f"Computer chose: {list[pc]}")

    if me == 0 and pc == 0:
        print("You win")
    elif me == 2 and pc == 0:
        print("You lost!")
    elif me > pc:
        print("You win!")
    elif me == pc:
        print("Draw!")
    else:
        print("You lost!")