# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!
a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
n = int(input("Введите значение n : "))

my_list = list(range(-n, n + 1))

print(f"Образовавшийся список : {my_list}")
len_list = len(my_list)

if len_list >= a > 0 and len_list >= b > 0:
    print(f"произведение элементов на указанных позициях : {my_list[a - 1] * my_list[b - 1]}")
else:
    print("There are no values for these indexes!")