documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
print(
    f'\nСписок возможных команд:\n'
    f'"p" – команда по номеру документа выведет имя человека, которому он принадлежит;\n'
    f'"l" – команда выведет список всех документов;\n'
    f'"s" – команда по номеру документа выведет номер полки, на которой он находится;\n'
    f'"a" – команда добавит новый документ;\n'
    f'"d" – команда по номеру документа удалит его;\n'
    f'"m" – команда по номеру документа переместит его с текущей полки на целевую;\n'
    f'"as" – команда добавит новую полку;'
)


def search_name_for_number():
    entered_number_doc = input('\nВведите номер документа: ')
    for elem in documents:
        if elem['number'] == entered_number_doc:
            print(f"Владелец документа: {elem['name']}")
            return
    print(f'Документа с номером {entered_number_doc} в каталоге нет\n')


def all_documents_list():
    print('\nСписок всех документов:')
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))


def search_shelf_for_number():
    entered_number_doc = input('\nВведите номер документа: ')
    for shelf, number in directories.items():
        for doc_number in number:
            if doc_number == entered_number_doc:
                print(f'Документ лежит на полке номер - {shelf}')
                return
    print(f'Документа с номером {entered_number_doc} на полках нет\n')


def new_document():
    print('\nВведите данные нового документа:')
    entered_type_doc = input('Тип документа - ')
    entered_number_doc = input('Номер документа - ')
    entered_name_owner = input('Имя владельца - ')
    entered_shelf_number = input('Номер полки, куда положить документ - ')
    if entered_shelf_number not in directories:
        print(f'Полки с номером {entered_shelf_number} нет, введите существующую полку, либо создайте новую')
        return
    for elem in documents:
        if elem['number'] == entered_number_doc:
            print(f'Документ с номером {entered_number_doc} уже существует')
            return
    documents.append({'type': entered_type_doc, 'number': entered_number_doc, 'name': entered_name_owner})
    directories[entered_shelf_number].append(entered_number_doc)
    print(f'Документ с номером {entered_number_doc} добавлен на полку {entered_shelf_number}')


def del_doc():
    print('\nКакой документ необходимо удалить?')
    entered_number_doc = input('Номер документа: ')
    for elem in documents:
        if elem['number'] == entered_number_doc:
            documents.remove(elem)
        else:
            print(f'Документа с номером {entered_number_doc} в каталоге нет\n')
            return
    for number_doc in directories.values():
        if entered_number_doc in number_doc:
            number_doc.remove(entered_number_doc)
    print(f'Документ {entered_number_doc} удален из каталога и с полки')


def move_doc():
    print('\nКакой документ необходимо переместить?')
    entered_number_doc = input('Номер документа: ')
    entered_shelf_number = input('Номер полки, куда переместить документ: ')
    if entered_shelf_number not in directories:
        print(f'Полки с номером {entered_shelf_number} нет, введите существующую полку, либо создайте новую')
        return
    for number_doc in directories.values():
        if entered_number_doc in number_doc:
            number_doc.remove(entered_number_doc)
            directories[entered_shelf_number].append(entered_number_doc)
            print(f'Документ перемещен на {entered_shelf_number} полку')
            return
    print(f'Документа с номером {entered_number_doc} не существует')


def add_shelf():
    entered_shelf_number = input('\nВведите номер новой полки: ')
    if entered_shelf_number in directories:
        print(f'Полка с номером {entered_shelf_number} уже существует')
        return
    if entered_shelf_number not in directories:
        directories[entered_shelf_number] = []
    print(f'Полка c номером {entered_shelf_number} добавлена')


while True:
    input_command = input('\nВведите команду, если нужно закончить введите "Exit": ')
    if input_command == "p":
        search_name_for_number()
    if input_command == "l":
        all_documents_list()
    if input_command == "s":
        search_shelf_for_number()
    if input_command == "a":
        new_document()
    if input_command == "d":
        del_doc()
    if input_command == "m":
        move_doc()
    if input_command == "as":
        add_shelf()
    if input_command == "exit":
        break
