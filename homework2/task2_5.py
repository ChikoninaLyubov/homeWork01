# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
num = int(input('Введите цифру : '))
num_list = list(range(num))
my_list = []
print(num_list)
from random import randrange

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    num_list[n_1], num_list[n_2] = num_list[n_2], num_list[n_1]

print(num_list)