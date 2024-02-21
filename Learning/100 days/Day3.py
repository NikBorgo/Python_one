#1st exercise (if, elif, else and f)
print("Thank you for choosing Borgo's pizza!")
size = input("Which size of pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want cheese? Y or N: ")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

#Mia soluzione
#if size == "S":
#    if add_pepperoni == "Y":
#        price += 2
#elif size == "M" or size == "L":
#    if add_pepperoni == "Y":
#        price += 3

#Sua soluzione
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3


if extra_cheese == "Y":
    price += 1

price = int(price)

print(f"The price of your pizza is €{price}.")
