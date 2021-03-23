from w6 import Animal
from random import randint
class Horse(Animal):

    def voice(self):
        super().voice('horse voice')

class Donkey(Animal):

    def voice(self):
        super(Donkey, self).voice('donkey voice')

class Mull(Donkey,Animal):
    pass
id = 0
class BookValidationException(Exception):
    def __init__(self,id, message):
        super(BookValidationException, self).__init__(f'Invalid Book{id}:{message}')


class PageCountError(BookValidationException):
    def __init__(self, id):
        super(PageCountError, self).__init__(id,'invalid name')


class Book:
    def __init__(self,len_page, years, author, price):
        global id
        self.id = id
        if len_page > 500:
            raise PageCountError(id)
        self.len_page = len_page

        if years < 2000 or years > 2020:
            raise BookValidationException(id)
        self.years = years

        self.author = author
        self.price = price
        id += 1
from abc import abstractmethod


class Animal:
    pass

class Pet(Animal):
    pass

class FeliniInterface():
    @abstractmethod
    def meow(self):
        raise NotImplemented
class CanineInterface():
    @abstractmethod
    def bark(self):
        raise NotImplemented

class Cat(Pet, FeliniInterface):
    def meow(self):
        print('cat say meow')



class Dog(Pet, CanineInterface):
    pass

class WildAnimal(Animal):
    pass

class Lion(WildAnimal):
    pass



class Matrix:
    def __init__(self, length=5, height=5, random_from=0, random_to=0):
        self.length = length
        self.data = []
        for _ in range(length):
            row = []
            for _ in range(height):
                row.append(randint(random_from, random_to))
            self.data.append(row)

    def __str__(self):
        res = ("# " * self.length) + '\n'
        for row in self.data:
            for item in row:
                res += f'{item} '
            res += "\n"
        res += ("# " * self.length) + '\n'
        return res

class InvalidMatrixError(Exception):
    def __init__(self):
        super().__init__('Invalid matrix')


def find_max(matrix: Matrix):
    if len(matrix.data) <= 0:
        raise InvalidMatrixError

    max = matrix.data[0]
    for row in matrix.data:
        for item in row:
            if item > max:
                max = item

    return max


if __name__ == '__main__':
    c = Lion()