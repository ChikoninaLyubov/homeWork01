# Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите натуральное число N: "))
def factor_nums(n):
    prime_factors = [] 
    for i in range(n-1, 1, -1):
        a = 2
        while a * a <= n:
            if n % a == 0:
                prime_factors.append(a)
                n //= a
            else:
                a += 1
        if n > 1:
            prime_factors.append(n)
            return prime_factors
print(f"Простые множители числа: {factor_nums(n)}")