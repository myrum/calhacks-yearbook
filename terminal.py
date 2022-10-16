"""
    ok here's what i'm thinking:
     - figure out how to make database in python??? 
     - enter in everyone's data (bulk loading if time)
     - then add in new spread assignment plus preferences for each member [the kinda hard part]
     - once done give assignments and add them to chosen member(s) [the hard part]

    for the query searching assignment:
     - filter based on week of current assignment
     - have spreads as dictionary, value is tuple (section editor, week)

    special stuff:
     - validate user input
     - have db regularly update the week the spread is on, have active/inactive col
     - add in week blocks for midterms, out of town/vacation
        - would have to calc when the week 3 & 4 would be and avoid those weeks
     - create a nice ui for it
     - make it available on a website, online db
     - Allow deletion of members and data
     - mass input members/spreads
     - extend to other teams, modify to allow team members who double and not have conflicts
"""
# reference db file idk if it will work
import db

# ------------------HELPER FUNCS------------------
def extract_team(opt):
    if (opt.upper() == 'D'):
        return "Design"
    elif (opt.upper() == 'P'):
        return "Photo"
    elif (opt.upper() == 'C'):
        return "Copy"
    else:
        print("Invalid letter, returning to menu")
        main()

# ------------------FUNCS TO CALL FOR EACH OPTION------------------

# ******OPT 1 - QUERY LIST OF MEMBERS******
# make it search by team
def get_members():
    def get_by_team():
        team = input("""
         Which team list do you want to see?\n
            D - design
            P - photo
            C - copy\n
         Please enter a letter: """)
        print("user sel: ", team)
        main()
    
    option = input("Would you like to the roster for a specific team [Y/N]: ")

    if(option.upper() == "Y"):
        get_by_team()
    else:
        print("db query for all entries")
        db.return_all()
        main()

# ******OPT 2 - LOOK UP MEMBER AND ADD DATA FOR THEM******
def add_data():
    print("\t I need a little info before you can add a spread assignment:\n")
    name = input("\t What is their name? ")
    team = input("""
         What team are they on?\n
            D - design
            P - photo
            C - copy\n
         Please enter a letter: """)
    
    print("searching for member...")
    # add in db query and tell user if person was found or not
    # if not found ask if they would like to try again
    # if no return to main()

    print("\t Now I need some info on the spread you want to add:\n")
    spread_name = input("\t What's the spread name? ")
    section_editor = input("\t Who is the section editor? ")
    week = input("""
         What week is the spread on?\n
            1 - week 1
            2 - week 2
            3 - week 3
            4 - week 4
            5 - week 5 (finished but not done)
            6 - Finished\n
            Please enter a number: """)
    print("Spread added to database :D")
    # !!!!!TEST DEBUG REMOVE LATER!!!!!
    print(spread_name, section_editor, week)
    main()


# ******OPT 3 - MAKE NEW MEMBER AND ADD TO DB******
# also remember to clean user input
def create_new_member():
    print("""
         Congrats on the new team member!
         I just need some info before creating an entry for them:\n """)
    name = input("\t What is their name? ")
    pronouns = input("\t What are their pronouns? ")
    team = input("""
         What team are they on?\n
            D - design ╰(*°▽°*)╯
            P - photo ( •̀ ω •́ )✧
            C - copy (❁´◡`❁)\n
         Please enter a letter: """)


    # !!!!!TEST DEBUG REMOVE LATER!!!!!
    print(name, pronouns, team)

    # put code in to create member mongo db don't fail me now
    record = {
        "name" : name,
        "pronouns" : pronouns,
        "team" : extract_team(team), 
        "spreads" : {}
    }

    db.insert_record(record)

    main()


# ------------------BEGINNING OF PROGRAM------------------
def main():
    print("Welcome to mur's b&g spread scheduler! It takes in member data and preferences and assigns a spread!\n")

    option = input("""
         Menu:\n
            1 - See list of current members
            2 - Enter a spread assignment for existing member
            3 - Create new member
            4 - Make spread assignment (non functional)
            5 - Exit\n
         Please input a number and press enter: """)

    selection = int(option)

    if (selection == 1):
        get_members()
    elif (selection == 2): 
        add_data()
    elif (selection == 3):
        create_new_member()
    elif (selection == 4):
        print("4")
    elif (selection == 5):
        print("\nThank you for using mur's scheduler.\nGoodbye and see you again soon (≧∇≦)ﾉ\n")
        quit()


if __name__=="__main__":
    main()