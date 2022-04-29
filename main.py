from Classes import BasicWord, Player
from utils import load_random_word

name = input('Введите имя игрока\n')
player = Player(name)
word = load_random_word()
print(f'Привет {name}!')
print(f'Составьте {word.count_subwords()} слов из слова {word.main_word}\nСлова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop/стоп"')
print('Поехали, Ваше первое слово?')


counter = 0  # счетчик количества правильных ответов
while counter < len(word.subwords):  # условие выполняется пока значение счетчика меньше количества подслов
    user_word = input().lower()  # пользователь вводит подслово
    if word.check(user_word) and player.check_word_in_used_words(user_word) is False:  # если подслово пользователя есть в списке подслов и оно не введено ранее
        print('Верно')
        player.add_word_in_used_words(user_word)
        counter += 1
    elif player.check_word_in_used_words(user_word) is True:
        print('Такое слово уже есть')
    elif user_word == 'стоп' or user_word == 'stop':
        break
    else:
        print('Неверно')

if counter == len(word.subwords):
    print('Слова закончились, игра завершена!')
    print(f'Вы угадали {player.get_amount_words()} слов')
else:
    print('Игра завершена!')
    print(f'Вы угадали {player.get_amount_words()} слов')




