class Animal:
    name = 'имя'
    weight = 0
    voice = 'голос'
    eat = False
    cut = False
    milk = False
    egg = False

    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self):
        self.eat = 'Ам-мням-ням!'


class Hoofed(Animal):
    def to_milk(self):
        self.milk = True

    def to_cut(self):
        self.cut = True


class Bird(Animal):
    def collect_eggs(self):
        self.egg = True


cow = Hoofed('Манька', 432, 'Муууу...')
sheep_1 = Hoofed('Барашек', 120, 'Бееее...!')
sheep_2 = Hoofed('Кудрявый', 112, 'Бе-беее!...')
goat_1 = Hoofed('Рога', 95, 'Мееее..!')
goat_2 = Hoofed('Копыто', 93, 'Ме-меее...!')
goose_1 = Bird('Серый', 5.6, 'Га!')
goose_2 = Bird('Белый', 4.8, 'Га-га!')
chicken_1 = Bird('Ко-Ко', 3.8, 'Кококо!')
chicken_2 = Bird('Кукареку', 3.2, 'Кукареку!')
duck = Bird('Кряква', 2.1, 'Кря!')
hoofed_dict = {'milk': [cow, goat_2], 'cut': [sheep_1, sheep_2, goat_1, goat_2]}
bird_list = [goose_1, goose_2, chicken_2, {'eggs': [chicken_1, duck]}]
all_animals_list = [cow, sheep_1, sheep_2, goat_1, goat_2, goose_1, goose_2, chicken_1, chicken_2, duck]

print('\n На ферме у Дяди Джо просто сумасшедший дом! Он наверное спит...')
for animal in all_animals_list:
    print(f'{animal.name} кричит от голода {animal.voice}')

print('\n Их срочно нужно покормить!!!')
for animal in all_animals_list:
    animal.feed()
    print(f'{animal.name} ест, только и слышно {animal.eat}')

print('\n А так же подоить, остричь...')
for milking in hoofed_dict['milk']:
    milking.to_milk()
    print(f'{milking.name} подоена, она {milking.voice} от облегчения!')
for hairy in hoofed_dict['cut']:
    hairy.to_cut()
    print(f'{hairy.name} острижен!')
print(' ...и собрать яйца!!!')
for layer in bird_list[3]['eggs']:
    layer.collect_eggs()
    print(f'У {layer.name} яйца собраны!')

total_weight = {'weight': 0, 'name': ''}
for animal in all_animals_list:
    if total_weight['weight'] <= animal.weight:
        total_weight['name'] = animal.name
    total_weight['weight'] += animal.weight
print(f"\n Самое тяжелое животное - {total_weight['name']}, вес всех животных {total_weight['weight']}")
