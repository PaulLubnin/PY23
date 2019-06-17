"""
Created on Mon Dec 10 09:30:53 2018

@author: AS
"""

import requests

token = ''


class User:

    def __init__(self, id):
        self.id = id

    def get_mutual_friends(self, friend_id):
        params = {
            'target_uid': friend_id,
            'access_token': token,
            'v': 5.92
        }
        url = ('https://api.vk.com/method/friends.getMutual')
        response = requests.get(url, params).json()
        return response

    def __and__(self, other):
        params = {
            'target_uid': other.id,
            'access_token': token,
            'v': 5.92
        }
        url = ('https://api.vk.com/method/friends.getMutual')
        response = requests.get(url, params).json()
        list_id = response['response']
        users = []
        for id in list_id:
            users.append(User(id))
        return users

    def __str__(self):
        return ('https://www.vk.com/id' + str(self.id))


me = User(1306975)

friend = User(905767)

print(me)

# -------------------------

import requests
from urllib.parse import urlencode

app_id = '6774902'
auth_url = 'https://oauth.vk.com/authorize?'

auth_data = {
    'client_id': app_id,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.92'
}
# print(auth_url + urlencode(auth_data))

# token = '333e5d97c31a8c8b889cb975eb28e4823496d5564c0d828e657e42548fd5c8b4736e19f3b65f9fa877978'
#
# params = {
#     'access_token': token_Dima,
#     'v': '5.92',
#     'source_uid': '9897521',
#     'target_uid': '230412273'
# }
# response = requests.get('https://api.vk.com/method/friends.getMutual', params)
# print(response.json())

# params_2 = {
#     'access_token': token_Dima,
#     'v': '5.92',
#     'user_id': '230412273'
# }
# info_users = requests.get('https://api.vk.com/method/users.get', params_2)

# print(info_users.json())


class User:

    token = '333e5d97c31a8c8b889cb975eb28e4823496d5564c0d828e657e42548fd5c8b4736e19f3b65f9fa877978'

    def __init__(self, user_id):
        self.user_id = user_id

    def __and__(self, other):
        token = self.token
        params = {
            'access_token': token,
            'v': '5.92',
            'source_uid': self.user_id,
            'target_uid': other.user_id
        }
        info_users = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return info_users.json()

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


dima = User(9897521)
vika = User(230412273)

print(dima & vika, '\n')

print(dima)

# _______________________________________________
import requests
from urllib.parse import urlencode
from pprint import pprint

# Получение токена
APP_ID = 6983672
BASE_URL = 'https://oauth.vk.com/authorize'
auth_date = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5,95',
}
# print('?'.join((BASE_URL, urlencode(auth_date)))) #ссылка на токен
token = 'c21a809ff12d54b6039d0ebb45d97e4d71ca96ce362e83f005572863da664e35b8a1a61f387610d705d64'

class VkUser:

    def __init__(self, user_id):
        self.user_id = user_id

    def __and__(self, other):
        params = {
            'target_uid': other.user_id,
            'access_token': token,
            'v': '5,95'
        }
        url = 'https://api.vk.com/method/friends.getMutual'
        response = requests.get(url, params).json()
        list_id = response['response']
        users = []
        for id in list_id:
            users.append(VkUser(id))
        return users

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


me = VkUser(102306997)
friend = VkUser(22590446)
pprint(me & friend)
print(me)



