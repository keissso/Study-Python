import time as tm
from data_Bank import DataBank

# Initialize the DataBank instance
db = DataBank()

#Data Base interface
def menu_interface():
    """Display the main menu and get the user's choice."""
    print("Data Bank:")
    print("---------------------")
    print("(1) Insert Information")
    print("(2) Update Email")
    print("(3) Find User")
    print("(4) Delete User")
    print("(5) Exit")
    print("---------------------")
    try:   #Tryes to imput the User choice
        choice = int(input(">> Choice (Num only): ")) 
        return choice
    except ValueError:
        print("Invalid input! Please enter a number.") 
        return None

#Menu Choices 
def menu_choices(choice):
    #Handles the User choice 
    if choice == 1:
        insert_info()
    elif choice == 2:
        update_email()
    elif choice == 3:
        find_user()
    elif choice == 4:
        delete_user()
    elif choice == 5:
        exit_menu()
    else:
        print("Invalid choice! Please select a valid option.")

#Input info in Data Base 
def insert_info():
    #Tryes to insert the user info to the Data Base
    try:
        name = input(">> Insert Name: ").strip()
        email = input(">> Insert Email: ").strip()
        user_id = int(input(">> Insert ID: "))
        db.add_user(user_id, name, email)
    except ValueError:
        print("Invalid input! ID must be a number.")
    return_menu()

#Update user Email
def update_email():
    #Updates a email of a exiting user 
    db.list_users() #lists all users 
    print("-------------------")
    try: #Tryes to update the new user email
        user_id = int(input(">> Insert the ID to update: "))
        new_email = input(">> Insert the new Email: ").strip()
        db.update_email(user_id, new_email)
    except ValueError: 
        print("Invalid input! ID must be a number.")
    return_menu()

#find user info 
def find_user():
    #Find user by name
    name = input(">> User Name: ").strip()
    db.find_by_name(name)
    return_menu()

#Delete User 
def delete_user():
    #Delete the seletected user from the Data Base 
    db.list_users()
    print("-------------------")
    try:
        user_id = int(input(">> Insert User ID to delete: "))
        db.delete_user(user_id)
    except ValueError:
        print("Invalid input! ID must be a number.")
    return_menu()

#Exits from Data base
def exit_menu():
    print("Exiting Data Bank...")
    tm.sleep(2)
    exit()

#returns to Data base menu 
def return_menu():
    #prompts the user to exit to the interface
    input(">> Press Enter to return to the menu...")

