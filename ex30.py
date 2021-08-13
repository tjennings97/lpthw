people = 30
cars = 40
trucks = 15


# if there are more cars than people
if cars > people: 
    print("We should take the cars.")
# if there are fewer cars than people
elif cars < people:
    print("We should not take the cars.")
# if there are equal cars and people    
else:
    print("We can't decide.")

# if there are more trucks than cars
if trucks > cars:
    print("That's too many trucks.")
# if there are fewer trucks than cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if there are equals trucks and cars
else: 
    print("We still can't decide.")

# if there are more people than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# if there are not more people than trucks (aka people less than or equal to trucks)
else: 
    print("Fine, let's stay home then.")