month = str(input('\nВведите Ваш месяц рождения: ').lower())
date = int(input('Введите Ваш день рождения: '))
if month == 'март' and date in range(21, 32) or month == 'апрель' and date in range(1, 21):
    print('\nВывод: Овен')
elif month == 'апрель' and date in range(21, 31) or month == 'май' and date in range(1, 21):
    print('\nВывод: Телец')
elif month == 'май' and date in range(21, 32) or month == 'июнь' and date in range(1, 22):
    print('\nВывод: Близнецы')
elif month == 'июнь' and date in range(22, 31) or month == 'июль' and date in range(1, 23):
    print('\nВывод: Рак')
elif month == 'июль' and date in range(23, 32) or month == 'август' and date in range(1, 24):
    print('\nВывод: Лев')
elif month == 'август' and date in range(24, 32) or month == 'сентябрь' and date in range(1, 24):
    print('\nВывод: Дева')
elif month == 'сентябрь' and date in range(24, 31) or month == 'октябрь' and date in range(1, 24):
    print('\nВывод: Весы')
elif month == 'октябрь' and date in range(24, 31) or month == 'ноябрь' and date in range(1, 23):
    print('\nВывод: Скорпион')
elif month == 'ноябрь' and date in range(23, 31) or month == 'декабрь' and date in range(1, 22):
    print('\nВывод: Стрелец')
elif month == 'декабрь' and date in range(22, 32) or month == 'январь' and date in range(1, 21):
    print('\nВывод: Козерог')
elif month == 'январь' and date in range(21, 32) or month == 'февраль' and date in range(1, 21):
    print('\nВывод: Водолей')
elif month == 'февраль' and date in range(21, 30) or month == 'март' and date in range(1, 21):
    print('\nВывод: Рыбы')
else:
    print('\nТакой даты нет')
