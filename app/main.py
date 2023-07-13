from app.services.io_file import get_path_if_file_exists, print_file_to_screen
from app.services.generate_users import generate_users, print_users
from app.services.api import print_info_from_api, get_info_from_api
from app.services.google import (
    get_google_sheets_pd_data,
    print_info_from_google_sheets_height,
    print_info_from_google_sheets_weight,
)


def main():
    # 1
    # Read file from project
    # read in folder files_input if present file .gitkeep
    file4output = "sample3.txt"
    # check if file exist
    link2file_output = get_path_if_file_exists(file4output)
    # output
    print_file_to_screen(link2file_output)

    # 2
    users = generate_users()  # default 100 users generated
    print_users(users, True)  # True print with first column Index

    # 3
    url1 = "http://api.open-notify.org/astros.json"
    # get data
    data = get_info_from_api(url1)
    # output
    print_info_from_api(data)

    # 4
    url2 = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    # get data
    df = get_google_sheets_pd_data(url2)
    # output
    print_info_from_google_sheets_height(df)
    print_info_from_google_sheets_weight(df)
