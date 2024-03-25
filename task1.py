import my_data as d


data = d.my_open()

while True:
    select = input(
        '1 - Додати посилання\n2 - Отримати посилання по назві\n3 - Вихід\n')
    if select == '1':
        d.my_add(data)
    elif select == '2':
        d.my_links(data)
    elif select == '3':
        break
