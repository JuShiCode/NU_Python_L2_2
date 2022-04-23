#Математические операции
a = int(input('First number '))
b = int(input('Second number '))
print('a+b=',a+b,' ', type(a+b), sep='')
print('a-b=',a-b,' ', type(a-b),  sep='')
print('a*b=',a*b,' ', type(a*b),  sep='')
print('a/b=',a/b,' ', type(a/b),  sep='')
print('a**b=',a**b,' ', type(a**b),  sep='')

#логические операции
a = True
b = False
#Отрицание
print('not a is', not a)
print('not b is', not b)
#Логическое "и"
print('a and b is', a and b)
#Логическое "или"
print('a or b is', a or b)

#Сравнение
a = int(input('Input number '))
print('a>100 is ', a > 100, sep='')
print('a<100 is ', a < 100, sep='')
print('a<=100 is ', a <= 100, sep='')
print('a>=100 is ', a >= 100, sep='')
print('a=100 is ', a == 100, sep='')
print('a!=100 is ', a != 100, sep='')