# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# stroka = input().split()
# res ={} # создаем пустой словарь 

# for i in stroka:
#     if i in res:
#         print(f'{i}_{res[i]}', end=' ')
#     else:
#         print(i, end=' ')        

#     res[i] = res.get(i, 0) + 1


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# stroka = "She sells sea shells on the sea shore The shells \
# that she sells are sea shells I'm sure.So if she sells sea \
# shells on the sea shore I'm sure that the shells are sea \
# shore shells"

# print(len(set(input().lower().split())))


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000  - 1
# while n != 0:
#     n = int(input())
#     if max_number > n:  - 2
#         max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)

n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if n > max_number:
        max_number = n
print(max_number)