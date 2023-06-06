names = {}
total_water = 'total_water'
sign = input("To signup please enter 'signup', if you already have an account enter 'login' "
"To quit enter 'quit'\n")
answer = None
if sign == "signup":
    name = input("please enter your name:\n")
    names[name] = {}
    names[name][total_water] = 0
    while answer != 'quit':
        print("To add a glass of water enter 'add' to quit use 'quit':")
        answer = input()
        if answer == "add":
            date = input("Enter date: \n")
            water = int(input("Enter amount of water bottles:\n"))
            names[name][date] = water
            names[name][total_water] = water
            answer = input("Would you like to add another? Yes/No? ")
            if answer == 'Yes':
                print("Type login to continue")
                sign = input()
                break
            else:
                exit(0)
        if answer == "quit":
            exit(0)
        else:
            print("Sorry I didn't understand try again:\n")
if sign == "login":
    print(names)
    while answer != 'quit':
        name = input("Please enter your name:\n")
        if name in names:
            print("Log in successful!")
        else:
            print("Sorry you need to signup first to use this program!")
            exit(0)
        answer = input("To add more water bottles type 'add' to quit use 'quit'")
        if answer == 'add':
            date = input("Enter date: \n")
            water = int(input("Enter amount of water bottles:\n"))
            names[name][date] = water
            names[name][total_water] += water
            print(f"total water {names[name][total_water]}")
        elif answer == 'quit':
            exit(0)
        else:
            answer = input("Sorry I didn't understand try again:\n")
else:
    exit(0)