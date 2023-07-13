from app.services.read_file import print_file
from app.services.generate_users import generate_users, print_users
from app.services.api import print_info_from_api
from app.services.google import print_info_from_google_sheets


def main():

    #1
    # Read file from project
    # read in folder files_input if present file .gitkeep
    print_file('sample3.txt')

    #2
    users = generate_users()
    print_users(users, True) #True print with first column Index

    #3
    print_info_from_api()

    #4
    print_info_from_google_sheets()



