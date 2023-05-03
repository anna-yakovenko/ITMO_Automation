# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# выведите в консоль значение аргумента Loc, объекта search

class Input:

    def __init__(self, loc, text): # атрибуты loc и text
        self.loc = loc
        self.text = text


search = Input('Input#search') # объект search как экземпляр класса Input, в скобках локатор
search_1 = Input('Input#search_1')

print(search.loc)
print(search_1.text)


class Button:

    def __init__(self, loc, text): # атрибуты loc и text
        self.loc = loc
        self.text = text


class Title:

    def __init__(self, loc, text): # атрибуты loc и text
        self.loc = loc
        self.text = text


class Link:

    def __init__(self, loc, text): # атрибуты loc и text
        self.loc = loc
        self.text = text

