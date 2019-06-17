import requests
import time
import json
import sys


def get_params(uid):
    return dict(
        access_token='73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1',
        user_id=uid,
        v=5.95
    )

def get_user_groups(uid):
    params = get_params(uid)
    response = requests.get('https://api.vk.com/method/groups.get', params=params)
    return set(response.json()['response']['items'])

def get_user_friends(uid):
    params = get_params(uid)
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    return set(response.json()['response']['items'])

def get_user_friends_groups(uid):
    user_friends_groups_list = []
    friends_groups_count = 1
    for friend_id in get_user_friends(uid):
        params = get_params(uid)
        params['user_id'] = friend_id
        response = requests.get('https://api.vk.com/method/groups.get', params=params).json()
        try:
            user_friends_groups_list.extend(response['response']['items'])
            time.sleep(0.5)
        except KeyError:
            if response['error']['error_code'] == 7:
                continue
            if response['error']['error_code'] == 18:
                continue
            if response['error']['error_code'] == 30:
                continue
            else:
                print('1 что то пошло не так')
        print('\r', end='')
        s = f'Подсчет групп {friends_groups_count} друга'
        sys.stdout.write(s)
        friends_groups_count += 1
    return set(user_friends_groups_list)

def get_info_about_only_user_groups(uid):
    groups = get_user_groups(uid).difference(get_user_friends_groups(uid))
    info_about_only_users_groups = []
    if len(groups) == 0:
        print('\nУникальных групп нет')
        pass
    else:
        groups_count = '.'
        for found_groups in groups:
            params = get_params(uid)
            params['group_id'] = found_groups
            params['sort'] = 'id_asc'
            response_info = requests.get('https://api.vk.com/method/groups.getById', params=params).json()
            response_members = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()
            try:
                groups_info_dict = {
                    'name': response_info['response'][0]['name'],
                    'gid': response_info['response'][0]['id'],
                    'members_count': response_members['response']['count']
                }
                info_about_only_users_groups.append(groups_info_dict)
                time.sleep(0.5)
            except KeyError:
                if response_members['error']:
                    groups_info_dict = {
                        'name': response_info['response'][0]['name'],
                        'gid': response_info['response'][0]['id'],
                        'members_count': 'не хватает прав доступа'
                    }
                    info_about_only_users_groups.append(groups_info_dict)
                    time.sleep(0.5)
                    continue
                else:
                    print('2 что то пошло не так')
            print('\r', end='')
            s = f'Обработка уникальной группы{groups_count}'
            sys.stdout.write(s)
            groups_count += '.'
        write_file(info_about_only_users_groups, 'groups.json')
    return info_about_only_users_groups

def write_file(what_write, where_write):
    with open(where_write, 'w', encoding='utf-8') as f:
        json.dump(what_write, f, ensure_ascii=False)
        print('\nПолученные данные записаны в файл')

def start_program():    #394105768  58306713
    input_user_id = int(input('\nДля начала работы введите числовой id пользователя Вконтакте: '))
    params = get_params(input_user_id)
    response = requests.get('https://api.vk.com/method/groups.get', params=params)
    try:
        if response.json()['error']:
            print('Не достаточно прав доступа!!!')
            start_program()
    except KeyError:
        if response.json()['response']:
            print('Для работы программы прав доступа достаточно')
        while True:
            print(
                f'\nДоступные команды:\n'
                f'"1" - количество групп пользователя\n'
                f'"2" - количество групп друзей пользователя\n'
                f'"3" - подсчет уникальных групп пользователя и запись данных о группе в файл\n'
                f'"e" - окончание работы\n'
            )
            input_command = input('Введите команду: ')
            if input_command == '1':
                print(f'Количество групп пользователя: {len(get_user_groups(input_user_id))}\n')
            elif input_command == '2':
                print(f'\nКоличество групп друзей пользователя: {len(get_user_friends_groups(input_user_id))}\n')
            elif input_command == '3':
                print(f'Всего уникальных групп пользователя: {len(get_info_about_only_user_groups(input_user_id))}\n')
            elif input_command == 'e':
                print('Работа завершена')
                break
            else:
                print('Такой команды нет!!!')


start_program()
