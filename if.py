#Оператор условия
brand = 'Volvo'     #марка
engine_volume = 1.5 #объём двигателя
horse_power = 152    #мощность двигателя
sunroof = True     #наличие люка

#Проверка условия if
if horse_power < 80: print('No tax')

#Проверка условия if/else
if horse_power < 80: print('No tax')
else: print('More tax')

#Проверка условия if/elif/else
if horse_power < 80:
    tax = 0
elif horse_power < 100:
    tax = 10000
elif horse_power < 150:
    tax = 20000
else:
    tax = 50000
print('tax=', tax, sep='')

#Проверка условия if для присваивания значения

# tax =
# print('tax=', tax, sep='')

cool_car = 0
cool_car = 1 if sunroof == 1 else 0
print (cool_car)
