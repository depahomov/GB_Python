# n = int(input())
# m = int(input())

# print((m+n-1)//n)

# Задача на сумму числе введённого числа:
# n = int(input("Введите число: "))
# summa = 1
# while n > 0:
#     x = n % 10
#     if x > 0:
#         summa *= x
#     n //= 10
# else:
#     print('Пожалуй, хватит')
# print(summa)

# Задача: пользователь вводит число,необходимо найти минимальный делитель данного числа:
# n = int (input("Введите число: "))
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print('Наименьший делитель числа ',n ,' => ',i )
#     elif i > n // 2:
#         print (n)
#         flag = False

#     i += 1

# Цикл for, функция range()
# r = 'qwerty'
# for i in r:
#     print(i) 


# line = ""
# for i in range(5):
#     line = ""
#     for J in range(5):
#         line += "*"
#     print(line)

text = 'Съешь ещё этих мягких французских булочек'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё', 'ЕЩЁ'))
text = text[2:9] + text[-5] + text[:2]
print(text)
