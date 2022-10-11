keys = ['Last Name', 'Name', 'Number']


def input_read(path):  # чтение данных из файла input.txt
    f = open(path, 'r', encoding='UTF8')
    temp = f.read().split('\n')
    f.close()
    lines = []
    for elem in temp:
        temp_dict = {}
        person = elem.split(' ')
        for i in range(len(person)):
            temp_dict[keys[i]] = person[i]
        lines.append(temp_dict)
    return lines


def write_data(data, path):  # перезапись из файла input в data
    f = open(path, 'w', encoding='UTF8')
    for line in data:
        temp = ''
        for element in line:
            temp += str(line[element]) + ' '
        f.writelines(temp[:-1] + '\n')
    f.close()


print(input_read('input.txt'))
write_data(input_read('input.txt'), 'data.txt')
