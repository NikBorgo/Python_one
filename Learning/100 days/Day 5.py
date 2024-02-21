# 1st exercise (for loops)
student_heights = input("Insert singular heights divided by space:\n").split()
for a in range(0, len(student_heights)):
    student_heights[a] = int(student_heights[a])

total_height = 0
number_people = 0
for height in student_heights:
    total_height += height
    number_people += 1
average_height= total_height / number_people

print(f"Total height: {total_height}")
print(f"Number of students: {number_people}")
print(f"Average height: {average_height}")

# 2nd exercise
scores = input("Insert singular heights divided by space:\n").split()
for a in range(0, len(scores)):
    scores[a] = int(scores[a])
highest = scores[0]
for b in range(0, len(scores)):
    if scores[b] > scores[b-1]:
        highest = scores[b]
print(f"The highest score in the classroom is: {highest}")

# 3rd exercise
number = 0
max_number = int(input()) + 1
for a in range(2, max_number, 2):
    number = number + a
print(number)

# 4th exercise
for a in range(1,101):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0:
        print("Fizz")
    else:
        print(a)

# Final exercise
import random

letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
simbols_list = ["!", "£,", "$", "%", "/", "(", ")"]
password_list = []
password = ""


print("Welcome to password generator")
letters = int(input("How many letters: "))
simbols = int(input("How many simbols: "))
numbers = int(input("How many numbers: "))

for letter in range(1, letters + 1):
    letter = random.randint(0, 23)
    letter = letters_list[letter]
    upper = random.randint(0, 1)
    if upper == 0:
        letter = letter.lower()
    password_list.append(letter)

for number in range(1, numbers + 1):
    number = str(random.randint(1, 10))
    password_list.append(number)

for simbol in range(1, simbols + 1):
    simbol = random.randint(0, 6)
    simbol = simbols_list[simbol]
    password_list.append(simbol)

random.shuffle(password_list)

for g in password_list:
    password += g


print(password)




