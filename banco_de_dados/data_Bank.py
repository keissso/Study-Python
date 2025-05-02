from datetime import datetime

data_bank = {}#

#Data bank imput
def data_imput(id, name, email): 
    if id in data_bank: 
        print(f"Id{id} already exists")
    else : 
        data_bank[id] = { 
            "Name" : name,
            "Email" : email,
            "Data" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"User{name}, sucefully registred!")

#Data bank listing of data
def listData():
    print("Users registred:")
    list(map(lambda item: print(f"Id: {item[0]}, Name:{item[1]['name']}, Email:{item[1]['email']}, Data:{item[1]['data']}"), data_bank.items()))

#Email update in Data bank
def Email_change(id, new_email): 
    if id in data_bank:
        data_bank[id]['email'] = new_email
        print("Email updated with sucess!")
    else: 
        print("User not found!")

#Delete user in Data bank 
def delete_user(id):
    if id in data_bank: 
        del data_bank[id]
        print(f"User {id} deleted with sucess!")
    else :
        print("User not found!")

#User by name in data bank
def find_by_name(name):
    result = list(filter(lambda x: x[1]['name'].lower() == name.lower(), data_bank.items()))
    if result: 
        print("results: ")
        list(map(lambda item: print(f"ID: {item[0]}, Name: {item[1]['name']}, Email: {item[1],['email']}, Data: {item[1]['data']}"), result))
    else: 
        print("User not found!")