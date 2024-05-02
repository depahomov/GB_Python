# СПИСКИ
# list_1 = []
# list_1 = list()
# # print(list_1)
# list_1 = [1, 2, 3, 8]
# # print(*list_1)

# for i in list_1:
#     print(i)

# print(list_1[-1])

# ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В СПИСОК
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# list_1.append(10)
# print(list_1)

# УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ СПИСКА
# list_1.pop()
# print(list_1)

# list_1.pop(3)
# print(list_1)

# list_1.insert(2, 15)
# print(list_1)

# t = () 
# print(type(t))

# КОРТЕЖИ
# t = (1, 5, 3,)
# print(t)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))


# # a, b, c = v
# # print(a, b, c)
# t[0] = 2

# СЛОВАРИ
# Создание пустого словаря
# d = {}
# d = dict()

# # Добавление значений
# d[1] = 'qwerty'
# # print(d)

# d[2] = 'werty'
# print(d[2])

# dictionary = {'up': 'вверх', 'left': 'влево', 'down': 'вниз', 'right': 'вправо'}
# print(dictionary.items())

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# for (k,v) in dictionary.items():
# print(k, v)

# del dictionary['left']
# print(dictionary)

# МНОЖЕСТВА
# colors = {'red', 'green', 'blue'}
# print(colors)

# colors.add('gray')
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c = {1, 2, 3, 5, 8}
# print(c)
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)
# q = a.union(b).difference(a.intersection(b))
# print(q) 

# list_1 = [(i, i) for i in range(1, 101) if i % 2 ==0]
list_1 = [i *2 for i in range(10) if i % 2 == 0]
print(list_1)