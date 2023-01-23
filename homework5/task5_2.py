# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

my_str = 'Абв ылоажы фыыдлх абв, Зщышф вабвв ффлжв абВ!'
# my_str = my_str.lower()

result_list = []
find = 'абв'
symb = ['.',',','!','?',':']
for s in symb:
    my_str = my_str.replace(s, ' '+ s + ' ')
new_list = my_str.split()   
print(new_list)


for item in new_list:
    if not find.lower() in item.lower():
        result_list.append(item)
print(' '.join(result_list))