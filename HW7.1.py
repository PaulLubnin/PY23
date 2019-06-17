print('\n Польская нотация. \nПример ввода оператора и операндов: + 2 2')
def polish_notation(operand):
    operand_list = operand.split(' ')
    assert len(operand_list) <= 3, 'Должен быть 1 оперотор и 2 операнда!'
    assert operand_list[0] == '+' or operand_list[0] == '-' or operand_list[0] == '*' or operand_list[0] == '/',\
        'Не подходящий операнд!'
    try:
        if operand_list[0] == '+':
            print(f'Ответ: {operand_list[1]} + {operand_list[2]} = {int(operand_list[1]) + int(operand_list[2])}')
        if operand_list[0] == '-':
            print(f'Ответ: {operand_list[1]} - {operand_list[2]} = {int(operand_list[1]) - int(operand_list[2])}')
        if operand_list[0] == '/':
            print(f'Ответ: {operand_list[1]} / {operand_list[2]} = {int(operand_list[1]) / int(operand_list[2])}')
        if operand_list[0] == '*':
            print(f'Ответ: {operand_list[1]} * {operand_list[2]} = {int(operand_list[1]) * int(operand_list[2])}')
    except Exception as e:
        print(f'{type(e)},{e}')


while True:
    polish_notation(input('Введите оператора и операндов через пробел: '))