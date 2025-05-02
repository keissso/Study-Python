from datetime import datetime

#Data bank class
class DataBank:
    def __init__(self):
        self.data_bank = {}

    #Check if User exits 
    def user_exists(self, user_id):
        if user_id not in self.data_bank:
            print(f"User with ID {user_id} not found!")
            return False
        return True
    
    #Adds User in the data Base 
    def add_user(self, user_id, name, email):
        if not isinstance(user_id, int) or not name or not email:
            print("Invalid input. Please provide a valid ID, name, and email.")
            return

        if user_id in self.data_bank: #Checks if user is in the Data Base 
            print(f"User with ID {user_id} already exists.")
        else:
            self.data_bank[user_id] = {
                "Name": name,
                "Email": email,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            print(f"User {name} successfully registered!")

    #Lists all users in the Data base 
    def list_users(self):
        if not self.data_bank: #checks if has all users info in the Data base
            print("No users registered.")
            return

        print("Users registered:") #If exists it returns 
        for user_id, details in self.data_bank.items():
            print(
                f"ID: {user_id}, Name: {details['Name']}, Email: {details['Email']}, Date: {details['Date']}"
            )

    #Updates email of the user 
    def update_email(self, user_id, new_email):
        if self.user_exists(user_id):  #If user exists it updates the user Email 
            self.data_bank[user_id]["Email"] = new_email
            print(f"Email for user ID {user_id} updated successfully!")

    #Deletes user in the Data base
    def delete_user(self, user_id):
        if self.user_exists(user_id):
            del self.data_bank[user_id]
            print(f"User with ID {user_id} deleted successfully!")

    #Finds user by name in the Data base 
    def find_by_name(self, name):
        results = [
            (user_id, details)
            for user_id, details in self.data_bank.items()
            if details["Name"].lower() == name.lower()
        ]
        if results: #If name has a result it returns all infos of him
            print("Results:")
            for user_id, details in results:
                print(
                    f"ID: {user_id}, Name: {details['Name']}, Email: {details['Email']}, Date: {details['Date']}"
                )
        else: #else it not returns 
            print(f"No users found with the name '{name}'.")
