class Book:

    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def _read_write(func):
        def wrapped(self):
            try:
                if isinstance(self.size, int) and self.size >= page >= 0:
                    func
                else:
                    raise PageNotFoundError
            except IndexError:
                raise PageNotFoundError
        return wrapped

    @_read_write
    def read(self, page):
                return self.content[page]

    @_read_write
    def write(self, page, text):
                self.content[page].append(text)


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author: str, year: int, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.author = author
        self.year = year
        self.bookmark = dict()

    def read(self, page):
        """возвращает страницу"""
        return super().read(page)

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if self.bookmark.get(person) is not None:
            return self.bookmark.get(person)
        else:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        try:
            del self.bookmark[person]
        except KeyError:
            raise NotExistingExtensionError

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.size = len(content) if content else size
        self.max_sign = max_sign if max_sign else 2000
        self.content = content if content else ['' for _ in range(size)]

    def read(self, page):
        """возвращает страницу с номером page"""
        return super().read(page)

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        try:
            if len(text) <= self.max_sign:
                self.content[page] = f'{self.content[page]}{text}'
            else:
                raise TooLongTextError
        except IndexError:
            raise PageNotFoundError


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        try:
            book.set_bookmark(self.name, page)
        except NameError:
            raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        try:
            return book.get_bookmark(self.name)
        except NameError:
            raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        try:
            book.del_bookmark(self.name)
        except NameError:
            raise NotExistingExtensionError


class BookIOErrors(Exception):
    """базовый класс для исключений при работе с библиотекой"""
    pass


class PageNotFoundError(BookIOErrors):
    """для ситуаций, когда методы обращаются к несуществующей странице"""
    pass


class TooLongTextError(BookIOErrors):
    """для ситуаций, когда записываемый текст не помещается на странице"""
    pass


class PermissionDeniedError(BookIOErrors):
    """для ситуаций, когда запись в книгу запрещена"""
    pass


class NotExistingExtensionError(BookIOErrors):
    """если вызываемый метод у класса книги отсутствует"""
    pass


person = Person('Pasha')
content = [1, 2]
notebook = Notebook('note', 2, 100, content)
print(notebook.read(1))
