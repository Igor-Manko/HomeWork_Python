import csv

table = ['Фамилия', 'Имя', 'Телефон', 'Должность', 'Зарплата']


def find_data():
    request = input('Введите значение для поиска: ')
    with open('data.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if request in line:
                discription = dict(zip(table, line))
                for key, value in discription.items():
                    print(f'{key}: {value}')
                print('Данные успешно найдены!')
    return request
