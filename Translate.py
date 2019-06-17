import requests

def translate_it(file_read, file_write, lang, translate_lang = 'ru'):

    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    langs = f'{lang}-{translate_lang}'

    with open(file_read) as text:

        params = {
            'key': key,
            'lang': langs,
            'text': text,
        }
        response = requests.get(url, params=params).json()
        translate_text = ' '.join(response.get('text', []))

    with open(file_write, 'w', encoding='utf8') as text:
        text.write(translate_text)


translate_it('DE.txt', 'DE-translated.txt', 'de')
translate_it('ES.txt', 'ES-translated.txt', 'es')
translate_it('FR.txt', 'FR-translated.txt', 'fr')