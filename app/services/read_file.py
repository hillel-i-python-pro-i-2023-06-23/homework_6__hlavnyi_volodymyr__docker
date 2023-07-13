from app.services.check_file_exists import get_path_if_file_exists

def print_file(name_of_file:str):

    txt_file = get_path_if_file_exists(name_of_file)
    with open(txt_file, 'r') as f:
        print(f.read())