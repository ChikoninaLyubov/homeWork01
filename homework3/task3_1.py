# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample

def my_list(count: int) -> list:
    if count < 0:
        print("Отрицательные значения : ")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_list(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums


all_list = my_list(int(input("Введите число определяющие длину списка: ")))
print(f'Получившийся список {all_list}')
print(f'Сумма эллементов с нечетным индексом = {sum_list(all_list)}')