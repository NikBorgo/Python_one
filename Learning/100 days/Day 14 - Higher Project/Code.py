import Project_list
import random

A = random.choice(Project_list.data)
B = random.choice(Project_list.data)
WINNER = 0
LOSER = 0
count = 0
playing = True

print("WELCOME TOOOOO \nGUESS WHO HAS MORE FOLLOWER!")


def compare(one, two):
    global WINNER
    if one["follower_count"] > two["follower_count"]:
        return A
    elif one["follower_count"] < two["follower_count"]:
        return B
    else:
        return 0

def turn():
    global WINNER
    global count
    global LOSER

    print(f"\nA: {A["name"]}, {A["description"]}, from {A["country"]}")
    print("VS")
    print(f"B: {B["name"]}, {B["description"]}, from {B["country"]}")

    WINNER = compare(one=A, two=B)
    if WINNER == 0:
        return True

    guess = input(f"\na'A' {A["name"]} or 'B' {B["name"]}:").lower()

    if guess == "a" and WINNER == A:
        count += 1
        print(f"\n Good!\n{A["name"]} with {A["follower_count"]} followers vs {B["name"]} with {B["follower_count"]} followers.")
        LOSER = B
        return True
    elif guess == "b" and WINNER == B:
        count += 1
        print(f"\n Good!\n{B["name"]} with {B["follower_count"]} followers vs {A["name"]} with {A["follower_count"]} followers.")
        LOSER = A
        return True
    else:
        print(f"{A["name"]} with {A["follower_count"]} followers vs {B["name"]} with {B["follower_count"]} followers.")
        print(f"You lost! You reached a score of {count}.")
        return False

while playing:
    playing = turn()
    if LOSER == A:
        A = random.choice(Project_list.data)
    else:
        B = random.choice(Project_list.data)


