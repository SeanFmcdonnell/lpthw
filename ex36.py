from sys import exit

def surf_time():
    print("Righteous decision.")
    print("Grab your board.")
    print("Get your bike.")
    print("Who are you going to call? John John, Kelly, or Steak Sauce?")
    call = False

    while True:
        choice = input("> ")

        if choice == "John John":
            lost("He's pumped to ride with you.")
        elif choice == "Kelly" and not call:
            print("Ride well. He may take you to surf ranch.")
        elif choice == "Steak Sauce" and call:
            lost("Prove yourself and you'll get to Costa Rica.")
        else:
            print("Who is that?")


def gym():
    print("Ok, fine then get to the gym.")
    print("No laying around in bed.")
    print("Are you going to lift weights or hit the treadmill?")

    choice = input("> ")

    if "lift" in choice:
        print("Swole is the goal, size is the prize.")
    elif "treadmill" in choice:
        lost("Make it ten miles.")
    else:
        gym()


def lost(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You wake up and check the surf report")
    print("The biggest waves of your life are outside")
    print("Are you going to surf?")

    choice = input("> ")

    if choice == "yes":
        surf_time()
    elif choice == "no":
        gym()
    else:
        print("It's a yes or no question...")
        start()


start()
