# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.
my_list = 1, 2, 3, 4, 5, 6, 7, 8, 9
my_sorted_list = []
my_new_list = []
for _ in my_list:
    if _ % 2 == 0:
        pass
    else:
        my_sorted_list.append(_)
for _ in my_sorted_list:
    my_new_list.append(_ * 2)
print(my_new_list)
