import json
import xml.etree.ElementTree as ET
import datetime
from pprint import pprint


class FileCreator:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, encoding='utf8')
        self.start_time = datetime.datetime.now()
        print(f'\nФайл {self.file} открыт в: {self.start_time}\n')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_time = datetime.datetime.now()
        self.delta = self.end_time - self.start_time
        print(f'\nФайл закрыт в: {self.end_time}')
        print(f'Время работы: {self.delta}')

def search_word():
    text_list.sort(key=len)
    for words in text_list:
        if len(words) >= 6:
            if words not in words_dicts.keys():
                words_dicts[words] = counter
            else:
                words_dicts[words] += 1

def top_10():
    top_words = {}
    top_words.update(dict(sorted(words_dicts.items(), key=lambda x: x[1], reverse=True)[:10]))
    print('Во всех новостях эти слова встречаются чаще всего.')
    for top, ten in top_words.items():
        print(top, '-', ten, 'раз(а)')


if __name__ == '__main__':
    with FileCreator('newsafr.json') as json_file:
        news_list = json.load(json_file)
        news_list = news_list['rss']['channel']['items']
        words_dicts = {}
        counter = 1
        for news in news_list:
            text_list = news['description'].lower().split(' ')
            search_word()
        top_10()

if __name__ == '__main__':
    with FileCreator('newsafr.xml') as xml_file:
        tree = ET.parse('newsafr.xml')
        news_list = tree.findall('channel/item/description')
        words_dicts = {}
        counter = 1
        for news in news_list:
            text_list = news.text.upper().split(' ')
            search_word()
        top_10()
