# # Задача 17. Сколько различных эл-тов в списке:
# a = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(a)))

# Задача 19. Сдвиг списка на k позиций вправо.
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)

# k = int(input())
# k = k % len(list_1)

# list_res = []

# for i in range(k):
#     list_res.append(list_1[len(list_1) - 1 - i])
# list_res.reverse()
# print(list_res)

# for i in range(len(list_1) - k):
#     list_res.append(list_1[i])
# print(list_res)

# Задача 21.
#  Печать всех уникальных значений в словаре
# list_1 = [{"v": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
#           {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]

# set_1 = set()

# for i in list_1:
#     for j in i:
#         set_1.add(i[j])

# print(set_1)

# Задача 23.
# Дан массив целых чисел. 
# Подсчитать кол-ко эл-тов массива, больших предыдущего (эл-та с предыдущим номером)
# list_1 = [0, -1, 5, 2, 3, 8]

# count = 0 
# for i in range(1, len(list_1)):
#     if list_1[i] > list_1[i - 1]:
#         count += 1

# print(count)

