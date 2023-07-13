from app.services.read_file import print_file
from app.services.generate_users import generate_users, print_users
from app.services.api import get_info_from_api, get_count_austronauts
from app.services.google import get_google_sheets_pd_data, get_from_pd_hight, get_from_pd_weight, \
    convert_inches_in_cm, convert_pounds_in_kg


def main():

    #1
    # Read file from project
    # read in folder files_input if present file .gitkeep
    print_file('sample3.txt')

    #2
    users = generate_users() #default 100 users generated
    print_users(users, True) #True print with first column Index

    #3
    #print_info_from_api()
    url = 'http://api.open-notify.org/astros.json'
    data = get_info_from_api(url)
    print(f'Now we have {get_count_austronauts(data=data)} austronauts in space')

    #4
    df = get_google_sheets_pd_data()
    print(f'Average hight is {convert_inches_in_cm(get_from_pd_hight(df=df))}')
    print(f'Average weight is {convert_pounds_in_kg(get_from_pd_weight(df=df))}')



