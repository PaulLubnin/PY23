documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "invoice", "number": "11-3"},
  {"type": "invoice", "number": "11-9"},
]

def name_list():
    try:
        for elem in documents:
            print(f"{elem['name']}")
    except KeyError:
        print('Ключа name не существует у документа!!!')


while True:
    input_command = input('Ввведите команду: ')
    if input_command == 'p':
        name_list()
    if input_command == 'q':
        break
