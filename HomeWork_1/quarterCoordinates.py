# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите четверть координат: '))


if quarter != 0 and quarter <= 4:
    if quarter == 1:
        print('X > 0, Y > 0')
    if quarter == 2:
        print('X < 0, Y > 0')
    if quarter == 3:
        print('X < 0, Y < 0')
    if quarter == 4:
        print('X > 0, Y < 0')
else:
    print('Введите четверть координат от 1 до 4')
