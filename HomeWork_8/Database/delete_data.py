import re


def delete():
    request = input('Введите данные для поиска и удаления: ')
    with open('data.csv', encoding='utf-8') as f:
        lines = f.readlines()
    str = request
    pattern = re.compile(re.escape(str))
    with open('data.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
                print('Данные удалены!')

    return request


"""
    with open('data.csv', 'rb', encoding='UTF=8') as file:
        reader = csv.reader(file, delimiter=',')
        # reader = pd.read_csv('data.csv')
        for line in reader:
            if request in line:
                print('Данные успешно удалены!')  # pass
    return request
"""