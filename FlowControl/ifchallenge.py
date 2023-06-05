name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
if 18 <= age <= 30:
    print("welcome club 18-30 holidays, {0}".format(name))
else:
    print("sorry we cannot allow bitches")