import datetime
"""
Program: bday.py
Autor: Brian

Displays a list of people's name. The user will type the name of one of the people, and the program will return that person's date of birth. If the user does not enter a valid name, the program will alert them of the error and re-display the menu.

"""
person = ""
#Gets todays month and day and turns it into a string
now = datetime.datetime.now()
month = str(now.month)
day = str(now.day)
today = month + "/" + day
#Dictonary of people and there birthdays
birthdays = {
    "Albert Einstein":"3/14/1879", 
    "Ben Franklin":"1/17/1706",
    "Bill Gates":"10/28/1995",
    "Plato":"424 BC",
    "Guido Van Rossum":"1/31/1956",
    "Brian McLaughlin":"5/25/1994",
    "John Wall":"9/6/1990"
}
#while loop so user can check as many birthdays as they want
while person != "quit":
    print("Welcome to the birthday directory. We know the birthdays of: ")
    #looks through birthdays and prints the key names
    for name in birthdays:
        print(name)
    #prompts user for who they would like to see
    person = input("Enter the name of whos birthday you want to know, or type 'quit' to leave >>>")
    #happens if person is in dictonary
    if person in birthdays:
        #if the birthday is equal to the current date displays a special message
        if today in birthdays[person]:
            print("Today is " + person +"'s Birthday. HAPPY BIRTHDAY")
        #displays the birthday
        else:
            print("{}'s birthday is {}!".format(person, birthdays[person]))
        print()
        print()
    #occurs if the person is not in the dictonary
    elif person != "quit":
        #Prompts user if they want to add the person to 'birthdays', if yes it stores the data
        print("We're sorry, we dont have a birthday for {}.".format(person))
        add = input("Do you know " + person + "'s birthday if so say yes to add it to the dictonary >> ")
        if add == "yes":
            bday = input("What is "+ person + "'s birthday (enter in x/x/xxxx format >>" )
            birthdays[person] = bday