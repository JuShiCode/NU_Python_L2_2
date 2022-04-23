#Цикл for
#
# for i in range(10): #range(start, stop, step)
#     print(i)
#     if i == 5: break
#

# for i in range(10):
#     answer = input('Какая лучшая марка автомобиля? ')
#     if answer == 'Volvo':
#         print('Вы абсолютно правы!')
#         break
#     else:
#         if i == 9:
#             print('Вы безнадёжны...')
#         else:
#             print('Нет, вы ошибаетесь, подумайте ещё')

for i in range(10):
    print(i)
    if i == 9: break
    if i < 3: continue
    else:
        print('Это число больше 3')
