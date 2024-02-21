#first exercise (data types: integer, float, boolean and string)
two_dig = input()
result = int(two_dig[0]) + int(two_dig[1])
print(result)

#final exercise (while loop)
print("Welcome to the tip calculator.")
bill = input("What was the total bill? €")
people = input("How many people to split the bill?")

while True:
    percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

    if percentage.isdigit():
        percentage = int(percentage)

        if percentage in [10, 12, 15]:
            break
        else:
            print("Sorry, you can only input 10, 12, or 15.")
    else:
        print("Sorry, please enter a valid number (10, 12, or 15).")

Individual_cost = (float(bill) / 100 * (percentage)) / int(people)
print(f"Each person should pay: €{Individual_cost:.2f}")

two_dig = input()
