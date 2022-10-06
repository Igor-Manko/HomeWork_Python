import write_data as wd
import read_data as rd
import delete_data as dd
import log


def ask_user():
    choise = input('Записать, найти или удалить данные (w/r/d): ')
    if choise == 'w':
        log.write_log(wd.get_data(), 'w')
    elif choise == 'r':
        log.write_log(rd.find_data(), 'r')
    elif choise == 'd':
        log.write_log(dd.delete(), 'd')
    else:
        print('Неизвестная команда')
        log.write_log(choise, 'Неизвестная команда')
