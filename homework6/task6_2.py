# 2. Для чисел в пределах от 20 до N найти числа, 
# кратные 20 или 21. Use comprehension.

def find_num():
    num = int(input("Input the last number of range: "))
    print([i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0])

find_num()