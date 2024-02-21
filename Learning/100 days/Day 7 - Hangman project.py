import random
easy_words = ["apple", "book", "cat", "dog", "house", "ball", "tree", "sun", "moon", "car", "train", "bird", "fish", "chair", "table", "pen", "paper", "hat", "shoe", "sock", "door", "window", "cup", "plate", "fork", "spoon", "knife", "banana", "orange", "grape"]
random_word = random.choice(easy_words)
n_blanks = len(random_word)


blank = "_" * n_blanks
print(blank)
blank_list = list(blank)
word_list = list(random_word)
errors = 0
end = False

while end == False:

    guess = input("guess a letter: ")
    index_of_value = []
    if guess not in word_list:
        errors += 1
    else:
        for i in range(len(random_word)):
            if word_list[i] == guess:
                blank_list[i] = guess
                # or letter = random_word[i]
                #    if letter == guess
                #         blank_list[i] = guess
    blank_up = "".join(blank_list)
    print(blank_up)
    print(errors)
    if "_" not in blank_up:
        end = True
        print(f"You won! The word is: {random_word}")
    if errors > 4:
        end = True
        print(f"You lost! The word is: {random_word}")