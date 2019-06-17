from pprint import pprint


def read_file():
    with open('recipes.txt', encoding='utf8') as cook_file:
        cook_book_dict = {}
        for line in cook_file:
            ingredients_list = []
            dish_name = line.strip()
            counter_ingredients = int(cook_file.readline().strip())
            for ing_line in range(counter_ingredients):
                ingredient = cook_file.readline().strip()
                ingredient_dict = {'ingredient_name': ingredient.split(' | ')[0],
                                   'quantity': ingredient.split(' | ')[1],
                                   'measure': ingredient.split(' | ')[-1]}
                ingredients_list.append(ingredient_dict)
            cook_file.readline().strip()
            cook_book_dict[dish_name] = ingredients_list
        return cook_book_dict


def cooking_list():
    cook_book = read_file()
    print('\nСписок блюд: ')
    for all_dish in cook_book.keys():
        print(all_dish)


def get_shop_list_by_dishes(input_dishes, person_count):
    cook_book = read_file()
    input_dish = input_dishes.split(', ')
    for dish in input_dish:
        d = dish.capitalize()
        if d not in cook_book.keys():
            print(f'{d} - нет в списке!')
            return
    cook_dict = {}
    for dishes in input_dish:
        d = dishes.capitalize()
        for dish, ing in cook_book.items():
            for ingredient in ing:
                if dish == d:
                    cook_dict[ingredient['ingredient_name']] = {ingredient['measure'],
                                                                int(ingredient['quantity']) * person_count}
    print(f'\nСпсиок необходимых продуктов на {person_count} гостей:')
    pprint(cook_dict)
    return


cooking_list()
get_shop_list_by_dishes(input('\nЧто будете готовить? Если блюд несколько, введите названия через запятую: '),
                        int(input('Какое количество гостей: ')))
