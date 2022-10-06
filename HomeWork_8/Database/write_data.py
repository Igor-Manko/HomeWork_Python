import csv

table = ['Фамилия', 'Имя', 'Телефон', 'Должность', 'Зарплата']


def get_data():
    record = [input(f'{i} :') for i in table]
    with open('data.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(record)
    print('Данные успешно записаны!')
    return record
