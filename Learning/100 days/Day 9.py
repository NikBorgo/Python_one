# 1st exercise (dictionaries)
# non lo posso fare perchè funziona con del codice nascosto
school_grades = {
    "jim" : 76
}

for key in school_grades:
    if school_grades[key] > 50:
        school_grades[key] = "passed"
    else:
        school_grades[key] = "not passed"

print (school_grades["jim"])

#2nd exercise (nested dictionaries)

#qui ci sarebbe da aggiungere i 3 input
travel_log = [
    {
        "country": "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    }
]

def add_country(cou, cit, tot):
    new_dictionary={}
    new_dictionary["country"] = cou
    new_dictionary["cities_visited"] = cit
    new_dictionary["total_visits"] = tot
    travel_log.append(new_dictionary)

#add_country(cou=country, cit=cities, tot=total_visits)
print(travel_log)

# Final exercise
not_finished = True
auction = {}
highest_bid = 0
winner_name = "none"

while not_finished:
    name = input("Insert name:")
    bid = int(input("insert bid:€"))
    auction[name]=bid
    clean_it = input("Are there any other people? 'Yes' or 'No':").lower()
    for i in auction:
        if auction[i] > highest_bid:
            highest_bid = auction[i]
            winner_name = str(i)
    if clean_it == "no":
        not_finished = False

print(f"The winner is {winner_name} with a bid of €{highest_bid}.")

print(auction)






