from app.config import FILES_INPUT_DIR

def check_file_exists():
    gitkeep_file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    if gitkeep_file_path.exists():
        return True
    else:
        return False

def get_path_if_file_exists(name_of_file:str):
    check_txt_file = FILES_INPUT_DIR.joinpath(name_of_file)
    if check_file_exists():
        return check_txt_file
    else:
        raise FileNotFoundError(f"File not found: {check_txt_file.as_uri()}")
