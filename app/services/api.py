import requests

def get_info_from_api(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_count_austronauts(data):
    return data['number']

def get_list_austronauts(data):
    list_astro=[]
    for a in data['people']:
        craft = a['craft']
        name_astro = a['name']
        list_astro.append( f'{craft} {name_astro}')
    return list_astro
def print_info_from_api():
    print_info_from_api_count_astro()
    print_list_austronauts()

def print_info_from_api_count_astro():
    url = 'http://api.open-notify.org/astros.json'
    data = get_info_from_api(url)
    print(f'Now we have {get_count_austronauts(data=data)} austronauts in space')

def print_list_austronauts():
    url = 'http://api.open-notify.org/astros.json'
    data = get_info_from_api(url)
    for count,astro in enumerate(get_list_austronauts(data=data)):
        print(count+1, astro)