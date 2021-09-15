from sys import exit

# ghosts of christmas past, present, and future
def ghost_of_xmas_future():
    print("You blink and the beggar shifts into the ghost of Christmas future.")
    print("She says, \"Congratulations, Scrooge. You've made it to the final stage.\"")
    print("She continues. \"We have nothing to show you. Now you will be tested. This is not a test of the mind. It's a test of the heart.\"")
    print("Suddenly a mirror appears and you're faced with no one but yourself.")
    print("You stare for what feels like hours and seconds simultaneously.")
    print("Suddenly the mirror disappears and a door appears. The question becomes clear.")
    print("Do you walk through the door as a changed individual or do you revert back you your old ways?")
    choice = input ("> ")

    if choice == "change":
        print("What an excellent decision. Best of luck on the rest of your journey.")
    else:
        print("What a shame. Good bye.")
        exit(0)

def ghost_of_xmas_present():
    print("The ghost of Chistmas past sweeps you up making you disoriented.")
    print("When you regain your wits, you're greeted by the ghost of Christmas present.")
    print("They show you a person asking for change. How much do you give?")
    amount = input("> ")

    while not amount.isdigit():
        print("Focus! Enter numbers only.")
        amount = input("> ")
    
    amount = int(amount)
    if amount < 100:
        print("Have you learned nothing? Good bye.")
        exit(0)
    else:
        print("Ah, that is a generous donation. This person surely appreciates it.")
        ghost_of_xmas_future()


def ghost_of_xmas_past():
    print("You're awaken by the ghost of Christmas past.")
    print("He shows you all the wrongs you've committed.")
    print("Do you show remorse or justify your actions?")
    action = input("> ")

    if action == "show remorse":
        print("There may be hope for you after all.")
        ghost_of_xmas_present()
    elif action == "justify my actions":
        print("You cannot be saved. Good bye.")
        exit(0)
    else:
        print("Let's repeat this adventure until you can provide a satisfactory answer.")
        ghost_of_xmas_past()

ghost_of_xmas_past()