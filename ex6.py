# assigning a value
types_of_people = 10
# creating a string using the variable above - f-string
x = f"There are {types_of_people} types of people."

# assigning variables
binary = "binary"
do_not = "don't"
# creating another f-string using variables above
y = f"Those who know {binary} and those who {do_not}."

# printing f-strings
print(x)
print(y)

# printing f-strings
# {x} is a variable that is a string that is created
#   using other variables aka a string inside a string
# same for {y} except {y} is in ''
print(f"I said: {x}")
print(f"I also said: '{y}'")

# more variable assignments
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# printing a string by fillining in the {} in joke_evaluation
#   with .format(). in this case the value of hilarious will
#   be inserted into the {}
print(joke_evaluation.format(hilarious))

# final set of variable assignments
w = "This is the left side of..."
e = "a string with a right side."

# printing the combination of strings w and e
print(w + e)
