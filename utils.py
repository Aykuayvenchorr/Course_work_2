import requests
import random
from Classes import BasicWord

response = requests.get('https://jsonkeeper.com/b/N1VN')
response_json = response.json()


def load_random_word():
    """Возвращает рандомное слово из внешнего ресусра"""
    word_random = random.choice(response_json)
    word_random = BasicWord(word_random['word'], word_random['subwords'])
    return word_random


