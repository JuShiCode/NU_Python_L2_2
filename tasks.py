#Задачи на циклы и оператор условия

'''Задача 1
Вывести на экран циклом пять строк из нулей,
чтобы каждая строка была пронумерована
'''
# i = 1
# while i <=5:
#     print(i, '00000')
#     i +=1
'''Задача 2
Пользователь в цикле вводит 10 цифр. 
Найти количество введённых пользователем цифр "5"
'''
# print('Сейчас вам будет предложено ввести 10 цифр. ')
# print('Вводите их по одной и ни о чём не беспокойтесь. ')
#
# n = 0       #счётчик введённых цифр
# fives = 0       #счётчик введённых пятёрок
#
# while n < 10:
#     number = int(input('Введите цифру: '))
#     if number == 5:
#         fives +=1
#         n +=1
#     else:
#         n += 1
# print('Введено пятёрок', fives)
'''Задача 3
Найти сумму ряда чисел от 1 до 100.
Полученный результат вывести на экран
'''
# sum = 0                 #переменная для текущей суммы в каждой итерации цикла
# for i in range(1,101):  #для чисел от 1 до 100
#     sum+=i              #к текущему значению суммы прибавляем текущее число
# print(sum)

'''Задача 4
Найти произведение ряда чисел от 1 до 10.
Полученный результат вывести на экран
'''
# product = 1
# for i in range(1, 11):
#     product *=i
# print(product)
# i = 1
# while i <= 10:
#     product *= i
#     i += 1
# print(product)

'''Задача 5
Вывести цифры числа в каждой строчке.
Только целые числа.
'''
#в обратном порядке
#integer_number = int(input('Введи целое число. '))
#в обратном порядке
# while integer_number > 0:
#     print(integer_number%10)
#     integer_number = integer_number//10
#в прямом порядке
# integer_number = str(integer_number)
# for i in range(len(integer_number)):
#     print(integer_number[i])
'''Задача 6
Найти сумму цифр числа
'''
# integer_number = int(input('Введи целое число. '))
# sum = 0
# while integer_number > 0:
#     sum += (integer_number%10)
#     integer_number = integer_number//10
# print(sum)
'''Задача 7
Найти произведение цифр числа
'''
# integer_number = int(input('Введи целое число. '))
# product = 1
# while integer_number > 0:
#     product *= (integer_number%10)
#     integer_number = integer_number//10
# print(product)
'''Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = int(input('Введи целое число. '))
# while integer_number > 0:
#     if (integer_number%10) == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else:
#     print('No')
'''Задача 9
Найти максимальную цифру в числе
'''
# integer_number = input('Введи целое число. ')
# max_digit = int(integer_number[0])
# i = 0
# while i < len(integer_number):
#     if max_digit >= int(integer_number[i]):
#         i +=1
#         continue
#     else:
#         max_digit = int(integer_number[i])
#         i +=1
# print(max_digit)

'''Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = int(input('Введи целое число. '))
# counter = 0
# while integer_number > 0:
#     if (integer_number % 10) == 5:
#         counter += 1
#     integer_number = integer_number//10
# if counter == 0:
#     print('No fives at all')
# else:
#     print(counter, 'fives')
