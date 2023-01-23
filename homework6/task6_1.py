# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import randint

def lists_func():
    num = int(input("Input the length of the wished list: "))
    ls = [randint(0, 99) for i in range(num)]
    print(ls)
    print([ls[i + 1] for i in range(num - 1) if ls[i] < ls[i + 1]])

lists_func()