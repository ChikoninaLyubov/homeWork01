# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

my_str = 'АБВ ылоажы фыыдлх абв, Зщышф вабвв ффлжв абВ!'
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