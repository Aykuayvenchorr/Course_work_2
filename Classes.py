class BasicWord:

    def __init__(self, main_word, subwords):
        self.main_word = main_word
        self.subwords = subwords

    def __repr__(self):
        return f'{self.main_word}: {self.subwords}'

    def check(self, user_word):
        """Проверяет, есть ли слово пользователя в подсловах"""
        return user_word in self.subwords

    def count_subwords(self):
        """Возвращает количество подслов"""
        return len(self.subwords)


class Player:

    def __init__(self, name):
        self.name = name
        self.users_words = []

    def get_amount_words(self):
        """Возвращает количество отгаданных слов"""
        return len(self.users_words)

    def add_word_in_used_words(self, word):
        """Добавляет подслово пользователя в список"""
        self.users_words.append(word)

    def check_word_in_used_words(self, word):
        """Проверяет, было ли введено ранее данное подслово"""
        return word in self.users_words
