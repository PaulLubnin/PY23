boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort(); girls.sort()
if len(boys) != len(girls):
    print('Кому-то не хватит пары!')
else:
    print('\nИдеальные пары:')
    for boy, girl in zip(boys, girls):
        print(boy, 'и', girl)