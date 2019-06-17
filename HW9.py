import random
import datetime

class FileCreator:

    def __init__(self, path):
        self.path = path
        self.start_time = datetime.datetime.now()
        print(f'\nНачало работы: {self.start_time}')

    def __enter__(self):
        self.file = open(self.path, 'w', encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_time = datetime.datetime.now()
        self.delta = self.end_time - self.start_time
        print(f'\nКонец работы: {self.end_time}')
        print(f'Время работы: {self.delta}')


if __name__ == '__main__':
    with FileCreator('random.txt') as file:
        cook_book = [
            ['салат',
             [
                 ['картофель', 100, 'гр.'],
                 ['морковь', 50, 'гр.'],
                 ['огурцы', 50, 'гр.'],
                 ['горошек', 30, 'гр.'],
                 ['майонез', 70, 'мл.'],
             ]
             ],
            ['пицца',
             [
                 ['сыр', 50, 'гр.'],
                 ['томаты', 50, 'гр.'],
                 ['тесто', 100, 'гр.'],
                 ['бекон', 30, 'гр.'],
                 ['колбаса', 30, 'гр.'],
                 ['грибы', 20, 'гр.'],
             ],
             ],
            ['фруктовый десерт',
             [
                 ['хурма', 60, 'гр.'],
                 ['киви', 60, 'гр.'],
                 ['творог', 60, 'гр.'],
                 ['сахар', 10, 'гр.'],
                 ['мед', 50, 'мл.'],
             ]
             ]
        ]
        person = int(input('\nКакое количество гостей? '))
        for dishes, ingredients in cook_book:
            print('\n', dishes.capitalize(), ':', sep='')
            for ingredient in ingredients:
                print(ingredient[0], ', ', ingredient[1] * person, ' ', ingredient[2], sep='')
        file.write(f'Было {person} гостей')


# ---------------------------------Контекст менеджер от Азарова Димы
#
# import datetime
#
# from contextlib import contextmanager
#
# @contextmanager
#
# def run_time():
#     try:
#         start_time = (datetime.datetime.now())
#         print(start_time)
#         yield
#     finally:
#         end_time = (datetime.datetime.now())
#         print(end_time)
#         print('Время на выполнение кода: {}'.format(end_time - start_time))