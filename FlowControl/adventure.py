available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break
else:
    print("aren't you glad you got out of there")
