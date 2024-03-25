import json


def my_open():
    try:
        with open('links.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return data

def my_add(data):
    link = input('Введіть посилання:\n')
    description = input('Введіть назву:\n')
    links_dict = {
        'link': link,
        'description': description
    }
    data.append(links_dict)
    with open('links.json', 'w') as f:
        json.dump(data, f, indent=4)

def my_links(data):
    description = input('Введіть назву:\n')
    for item in data:
        try:
            if item['description'] == description:
                print(f"Знайдено посилання: {item['link']}")
        except:
            print('Посилання з такою назвою не знайдено.')


