#Динамическая типизация
#
# temp_var_1 = input('Input something! ')
# print(temp_var_1, 'type', type(temp_var_1), 'id', id(temp_var_1))
#
# temp_var_2 = input('Input something else. ')
# print(temp_var_2, 'type', type(temp_var_2), 'id', id(temp_var_2))
#
# # temp_var_1=temp_var_2
# temp_var_1=int(temp_var_2)
# print(temp_var_1, 'type', type(temp_var_1), 'id', id(temp_var_1))

#Приведение типов
#для целых чисел
temp_int = input('Input integer ')
print('temp_int=', temp_int, 'type', type(temp_int), 'id', id(temp_int))

if temp_int.isdigit(): #работает только с целыми числами
    temp_int = int(temp_int)
    print('temp_int=', temp_int, 'type', type(temp_int), 'id', id(temp_int))
else:
    print('It is not a number!')

#для десятичных дробей
def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

temp_float = input('Input float number ')
print('temp_float=', temp_float, 'type', type(temp_float), 'id', id(temp_float))

if is_digit(temp_float): #работает только с целыми числами
    temp_float = float(temp_float)
    print('temp_float=', temp_float, 'type', type(temp_float), 'id', id(temp_float))
else:
    print('It is not a number!')