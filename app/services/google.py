import pandas as pd
from app.config import FILES_OUTPUT_DIR


def get_google_sheets_pd_data():
    url = 'https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt'
    #response = requests.get(url)
    #assert response.status_code == 200, 'Wrong status code'

    csv_file_path = FILES_OUTPUT_DIR.joinpath("gtable.csv")
    df = pd.io.parsers.read_csv(url)
    # wtite for testinf purpose
    df.to_csv(csv_file_path)

    return df

def get_from_pd_hight(df):
    hight_mean = df[['Height(Inches)']].mean()
    return hight_mean.values[0]

def get_from_pd_weight(df):
    weight_mean = df[['Weight(Pounds)']].mean()
    return weight_mean.values[0]

def convert_inches_in_cm(inches):
    return inches * 2.54

def convert_pounds_in_kg(pounds):
    return pounds * 0.453592

def print_info_from_google_sheets():
    df = get_google_sheets_pd_data()
    print(f'Average hight is {convert_inches_in_cm(get_from_pd_hight(df=df))}')
    print(f'Average weight is {convert_pounds_in_kg(get_from_pd_weight(df=df))}')


