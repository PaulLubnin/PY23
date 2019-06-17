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
