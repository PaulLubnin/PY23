import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

header = flats_list.pop(0) # "вытаскивание" 1го пункта из списка
print('Всего квартир: {}\n'.format(len(flats_list))) # подсчет квартир без 1го пункта

# подсчет новостроек в списке квартир
counter = 0
print('Новостройки:')
for index, flat in enumerate(flats_list, 1):
  if 'новостройка' in flat:
    print('№ {}'.format(index))
    counter += 1
print('Всего новостроек: {}\n'.format(counter))

# создание словаря из списка квартир
flat_info = {'ИД': flat[0], 'Комнат': flat[1], 'Н/В': flat[2], 'Стоимость': flat[11]}
# print(flat_info)

# создание словаря с ключом "метро", со значением в виде списка из словарей
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace('м.', '')
  flat_info = {'ИД': flat[0], 'Комнат': flat[1], 'Н/В': flat[2], 'Стоимость': flat[11]}
  if subway not in subway_dict.keys():
    subway_dict[subway] = list()
  subway_dict[subway].append(flat_info)
# print(subway_dict)

# подсчет (в словаре) количества квартир у метро
for name, value in subway_dict.items():
    print('У метро {} {} квартир(ы)'.format(name or '-', len(value)))