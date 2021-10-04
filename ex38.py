ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # call pop on more_stuff
    # pop(more_stuff) # call pop with argument more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one) # call append on stuff with argument next_one
    # append(stuff, next_one) # call append with arguments stuff and next_one
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop()) # call pop on stuff
# pop(stuff) # call pop with arument stuff
print(' '.join(stuff)) # what? cool! # call join on ' ' with argument stuff
# join(' ', stuff) # call join with arguments ' ' and stuff <- doesn't work, use above way
print('#'.join(stuff[3:5])) # super stellar! # call join on '#' with argument stuff[3:5]
# join('#', stuff[3:5]) # call join with arguments '#' and stuff[3:5]