# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def neg_fib(num: int):
    a, b = 1, 1
    my_list = [0]

    for i in range(num):
        my_list.append(a)
        my_list.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return my_list


print(*neg_fib(int(input('Введите число : '))))