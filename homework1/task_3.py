# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x = int(input('Введите число певой точки координаты : '))
y = int(input('Введите число второрой точки координаты : '))
if x > 0 and y > 0:
    print('на певой четверти')
elif x < 0 < y:
    print('на второй четверти')
elif x < 0 and y < 0:
    print('на третьей четверти')
elif x > 0 > y:
    print('на четвертой четверти')
else:
    print("Точка лежит оси")