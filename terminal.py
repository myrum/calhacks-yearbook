"""
    ok here's what i'm thinking:
     - figure out how to make database in python??? 
     - enter in everyone's data (bulk loading if time)
     - then add in new spread assignment plus preferences for each member
     - once done give assignments and add them to chosen member(s) [the hard part]

    special stuff:
     - validate user input
     - add in week blocks for midterms, out of town/vacation
        - would have to calc when the week 3 & 4 would be and avoid those weeks
     - create a nice ui for it
     - make it available on a website, online db
     - Allow deletion of members and data
     - mass input members/spreads
     - extend to other teams, modify to allow team members who double and not have conflicts
"""

# FUNCS TO CALL FOR EACH OPTION

# OPT 3 - MAKE NEW MEMBER AND ADD TO DB
# also remember to clean user input
def create_new_member():
    print("\
            Congrats on the new team member! \n\
            I just need some info before creating an entry for them:\n ")
    name = input("\tWhat is their name? ")
    pronouns = input("\tWhat are their pronouns? ")
    team = input("\
                    What team are they on? \n \
                    D - design ╰(*°▽°*)╯ \n \
                    P - photo ( •̀ ω •́ )✧ \n \
                    C - copy (❁´◡`❁) \n \
                    Please enter a letter: ")

    # TEST DEBUG REMOVE LATER
    print(name, pronouns, team)
    quit()
    # put code in to create member

# BEGINNING OF PROGRAM
print("Welcome to mur's b&g spread scheduler! It takes in member data and preferences and assigns a spread!\n\n")


option = input("\
                Menu: \n\n \
                1 - See list of current members \n \
                2 - Enter data for existing member \n \
                3 - Create new member \n \
                4 - Make spread assignment \n \
                5 - Exit \n\n \
                Please input a number and press enter: ")

selection = int(option)

if (selection == 1):
    print("u sel 1")
elif (selection == 2): 
    print("u sel 2")
elif (selection == 3):
    print("3")
    create_new_member()
elif (selection == 4):
    print("4")
elif (selection == 5):
    print("Thank you 4 using mur's scheduler.\nGoodbye and see u again soon (≧∇≦)ﾉ\n")
    quit()
