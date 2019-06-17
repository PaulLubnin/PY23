import requests
from pprint import pprint
from urllib.parse import urlencode

### Работа с библиотекой requests, http запросы
# URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
# text = 'я супер программист'
# params = {
#     'id': 'b3976a61.5cd9a802.81f8ca52-5-0',
#     'srv': 'tr-text',
#     'lang': 'ru-en'
# }
# data = {
#     'text': text
# }
# resp = requests.post(URL, params=params, data=data)
# print('1', resp)
# print('2', resp.text)
# print('3', f'Новый текст был: "{resp.json()["text"][0]}"')
# print('4', resp.json())


# URL = 'https://itunes.apple.com/search'
# params = {
#     'term': 'billy idol'
# }
# resp = requests.get(URL, params=params)
# pprint(resp.json())


### Работа с классами на примере API VK
APP_ID = 6983672
BASE_URL = 'https://oauth.vk.com/authorize'
auth_date = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status',
    'response_type': 'token',
    'v': '5,95',
}

# print('?'.join((BASE_URL, urlencode(auth_date))))

TOKEN = '823aa17e6d013be9f8838286345b526fc0b5acfaebc0e5b94e8573492aef746b53223814414c595c64776'

# params = {
#     'access_token': TOKEN,
#     'v': '5,95'
# }
#
# response = requests.get('https://api.vk.com/method/status.get', params=params)
# pprint(response.json())
#
# params['text'] = 'ololo'
# response = requests.get('https://api.vk.com/method/status.set', params=params)
# pprint(response.json())

class User:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        return dict(
            access_token=self.token,
            v='5.95'
        )

    def get_info(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/users.get', params=params)
        return response.json()

    def get_status(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/status.set', params=params)
        return response.json()

    def set_status(self, text):
        params = self.get_params()
        params['text'] = text
        response = requests.get('https://api.vk.com/method/status.set', params=params)
        return response.json()


masha = User(TOKEN)
pprint(masha.get_info())
pprint(masha.get_status())
pprint(masha.set_status('blablabla'))