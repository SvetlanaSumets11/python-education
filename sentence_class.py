"""This module is used to practice creating iterators and generators."""
from string import punctuation
import re


class SentenceIterator:
    """This class is an iterator for a class Sentence.
    Allows the class Sentence to be used as an iterable"""
    def __init__(self, words):
        """Initializing the fields of the class"""
        self.__words = words
        self.__index = 0

    @property
    def words(self):
        """Special functionality to a method words so that it acts like a getter."""
        return self.__words


    def __next__(self):
        """Method must return the next item in the sequence"""
        try:
            part = self.words[self.__index]
        except IndexError as error:
            raise StopIteration("Остановка итерации") from error
        self.__index = self.__index + 1
        return part


class Sentence:
    """This is the string class"""
    def __init__(self, string):
        """Initializing the fields of the class,
        check the validity of the entered data"""
        if isinstance(type(string), str):
            raise TypeError("Передана не строка")

        if string[-1] not in [".", "!", "?"]:
            raise ValueError("Предложение не имеет окончания")

        self.string = string

    def mass_words(self):
        """A generator for elementwise return of list items"""
        for part in re.findall(r'\w+', self.string):
            yield part

    @property
    def words(self):
        """Special functionality to a method words so that it acts like a getter."""
        return list(self.mass_words())

    def mass_other_chars(self):
        """A generator for elementwise return of list items"""
        for part in self.string.split(' '):
            if part[-1] in punctuation:
                yield part[-1]

    @property
    def other_chars(self):
        """Special functionality to a method words so that it acts like a getter."""
        return list(self.mass_other_chars())

    def __getitem__(self, key):
        """Method is usually used for list indexing"""
        return self.words[key]

    def __repr__(self):
        """responsible for the string representation of the object"""
        return f"words = {len(self.words)}, other chars = {len(self.other_chars)}"

    def __iter__(self):
        """Returns the corresponding iterator object"""
        return SentenceIterator(self.words)


sen = Sentence("Я люблю жизнь - это классно!")
print(sen)

print(sen.mass_words())
print(next(sen.mass_words()))

print(sen.words)
print(sen.other_chars)

print(sen[1])
print(sen[1:3])

for word in sen.words:
    print(word)

print(iter(sen))
for item in sen:
    print(item)
