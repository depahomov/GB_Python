# def f(x):
#     return x*x

# a = f
# print(type(a))
# print(a(5))
# print(f(6))

# # def calk1(a, b):
# #     return a + b
# # =>
# # calk1 = lambda a,b: a + b, 5, 45
# # =>

# # def calk2(a, b):
# #     return a * b
# # =>
# # calk2 = lambda a,b: a * b, 5, 45
# # =>

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)
# math(lambda a,b: a * b, 5, 45)

# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i*2))

# print(res)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = ['1', '2', '3', '5', '8', '15', '23', '38']
# # print(type(data[0]))
# res = select(int, data)
# # print(res)
# res = where(lambda x: x % 2 == 0, res)
# # print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# Есть набор данных. Функция map позволяет увеличить каждый объект на 10.

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем список из
# значений строки, пример:
# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
# 2. Теперь вернемся к задаче. С помощью функции map():
# data = list(map(int,input().split()))

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int, data.split()))
# print(data)

## Вывод чётных чисел из диапазона от 1 до 10
# data = [x for x in range(1, 11)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)

# # # Вывести числа, оканчивающиеся на 5
# # data = [15, 65, 9, 36, 175]
# # res = list(filter(lambda x: x % 10 == 5, data))
# # print(res)

# data = ['1', '2', '3', '5', '8', '15', '23', '38']
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#  Функция zip
# # Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# # Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# # функция enumerate
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

# # Файлы
# colors = ['red','green','5465465']
# data = open('file.txt', 'a') # указываем режим, в котором будем работать
# data.writelines(colors)     # разделителей не будет
# data.close()                # после файл надо закрыть

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
# # файл закрывается после выполнения with
# print(data) 
# ● Чтение данных из файла:
import os
print(os.getcwd())
path = 'O:\VSCode\Python_course\Project002'
os.chdir(path)
print(os.getcwd())

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    data.write('line 3\n')

data1 = open('file.txt', 'r')
for line in data1:
    print(line)
data1.close()

print(os.path.basename('O:/VSCode/Python_course/Project002/file.txt'))
print(os.path.abspath('file.txt'))