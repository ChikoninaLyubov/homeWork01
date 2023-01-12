# 1. Вычислить число c заданной точностью d
from decimal import Decimal, getcontext

number = Decimal(input("Введите число: "))
accuracy= Decimal(input("Введите требуемую точность '0.0001': "))

def num_accuracy(n, a):

    print("Число с заданной точностью: ", n.quantize(a))

num_accuracy (number, accuracy)