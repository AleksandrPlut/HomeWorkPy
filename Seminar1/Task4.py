# Задача 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_coord = int(input('Введите номер четверти координатной плоскости: '))
while quarter_coord < 1 or quarter_coord > 4:
    print('Такой четверти в плоскости координат нет, ввидети номер от 1 до 4')
    quarter_coord = int(input())

if quarter_coord == 1:
    print('x > 0, y > 0')
elif quarter_coord == 2:
    print('x < 0, y > 0')
elif quarter_coord == 3:
    print('x < 0, y < 0')
elif quarter_coord == 4:
    print('x > 0, y < 0')
