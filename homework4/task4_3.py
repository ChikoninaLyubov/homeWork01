# 3.Задайте последовательность чисел. Напишите программу,которая 
# выведет список неповторяющихся элементов исходной последовательности
#  в том же порядке.
from random import randint

num = int(input("Введите длину списка: "))
if num < 1:
    print("Вы ввели отрицательное значение количества чисел!")

num_list = []
for i in range(num):   
    num_list.append(randint (0, 9))  
print(num_list)

temp = {}
for i in num_list:
    if i in temp:
        temp[i] = False
    else:
        temp[i] = True

output = [i for i in temp if temp[i]]

print(f"Cписок неповторяющихся элементов исходной последовательности:\n{output}")
