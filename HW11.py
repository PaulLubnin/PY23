import requests
API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text_path, translated_text_path, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param from_lang:
    :return:
    """

    with open(text_path) as text:

        params = {
            'key': API_KEY,
            'text': text,
            'lang': '{}-{}'.format(from_lang, to_lang),
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        translated_text = ''.join(json_['text'])

    with open(translated_text_path, 'w', encoding='utf8') as text:
        text.write(translated_text)


translate_it('DE.txt', 'DE_translated.txt', 'de')
translate_it('ES.txt', 'ES_translated.txt', 'es')
translate_it('FR.txt', 'FR_translated.txt', 'fr')
print('Переводы записаны в файлы')