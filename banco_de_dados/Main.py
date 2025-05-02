import data_bank_interface as dbi

try:
    while(True):
        choice = dbi.menu_interface()
        dbi.menu_choices(choice)
except:
    print("Erro Ocurred, Try again!")