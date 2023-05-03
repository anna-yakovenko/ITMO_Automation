num_float = 8

# также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('число отрицательное')

permit_print = True
num = 3
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

x = -200
if x > 100 or x< -100:
    print('-')
else:
    print('+')

course_year = 5
if course_year >= 1 and course_year <= 4:
    print('бакалавр')
elif course_year >= 5 and course_year <= 6:
    print('магистр')
elif course_year >=7 and course_year <= 9:
    print('аспирант')
else:
    print('Введите корректный год обучения')