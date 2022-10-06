from datetime import datetime


def write_log(data, mode):
    if mode == 'w':
        edit_log(f'{datetime.now().strftime("%H:%M %d-%m-%Y")}: Запись данных -> {data}\n')
    elif mode == 'r':
        edit_log(f'{datetime.now().strftime("%H:%M %d-%m-%Y")}: Поиск данных -> {data}\n')
    elif mode == 'd':
        edit_log(f'{datetime.now().strftime("%H:%M %d-%m-%Y")}: Удаление данных -> {data}\n')
    else:
        edit_log(f'{datetime.now().strftime("%H:%M %d-%m-%Y")}: Неизвестная команда -> {data}\n')


def edit_log(text):
    with open('log.txt', 'a', encoding='UTF=8') as file:
        file.write(text)
