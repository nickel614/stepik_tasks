import time
class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.max_size = max_size if max_size else Matrix.MAX_SIZE
        self.matrix = [[None]]
        self.size = len(self.matrix)

    def __str__(self):
        s = '\n'.join([''.join([f'{n} ' for n in row]) for row in self.matrix])
        return s

    @staticmethod
    def _full_mass_iterator(size):
        for i in range(size):
            for j in range(size):
                yield i, j

    @staticmethod
    def _matrix_shift(m):
        """
        Сдвигает элементы в матрице после ее расширения так, чтобы не оставалось пробелов.
        :param m:
        :return:
        """
        size = len(m)
        for i in range(len(m) - 1)[:-1]:
            nones = m[i].count(None)
            for j in range(nones):
                m[i].remove(None)
            for j in range(nones):
                m[i].append(m[i + 1][j])
            for j in range(nones):
                m[i + 1].pop(0)
                m[i + 1].append(None)
        return m

    @staticmethod
    def _matrix_expanding(m):
        """Увеличивает размер квадратной матрицы на 1."""
        size = len(m)
        m.append([])
        for i in range(size):
            m[len(m) - 1].append(None)
        for i in range(len(m)):
            m[i].append(None)
        return m

    @staticmethod
    def _put_in_matrix(m, element):
        """Добавляет элемент в матрицу. Ищет первый not None элемент, начиная с конца."""
        i1 = j1 = len(m)**2 - 1
        iter = list(Matrix._full_mass_iterator(len(m)))
        for i, j in iter[::-1]:
            if m[i][j] is not None and m[i1][j1] is None:
                m[i1][j1] = element
                return m
            i1 = i
            j1 = j

    @staticmethod
    def _matrix_reduction(self):
        """Сокращает размер матрицы на 1."""
        m1 = []
        for i, j in self._full_mass_iterator(self.size):
            if self.matrix[i][j] is None:
                self.size -= 1
                break
            m1.append(self.matrix[i][j])
        self.matrix = [[None for j in range(self.size)] for i in range(self.size)]
        for i, j in self._full_mass_iterator(self.size):
            try:
                self.matrix[i][j] = m1.pop(0)
            except:
                return self.matrix

    @staticmethod
    def _append_in_base_matrix(self, element) -> object:
        """Добавляет элемент в матрицу размером 1х1"""
        if self.size == 1:
            self.matrix[0][0] = element
            self._matrix_expanding(self.matrix)
            self._matrix_shift(self.matrix)
            self.size += 1
            return self.matrix

    def pop(self) -> object:
        """
        метод возвращает удаленный элемент из матрицы, находящийся в ее конце
        :return:
        """
        if self.size == 1:
            raise IndexError
        m = self.matrix

        prev, i1, j1 = None, 0, 0
        for i, j in self._full_mass_iterator(self.size):
            if prev is not None and m[i][j] is None:
                popped = prev
                m[i1][j1] = None
                if i*self.size + j == (self.size-1)**2 - (self.size-1) + 1:
                    m = Matrix._matrix_reduction(self)
                return popped
            prev = m[i][j]
            i1 = i
            j1 = j

    def append(self, element=None) -> list:
        """
         Добавляет элемент element в матрицу и возвращает ее. Если последний элемент попадает в последнюю строку
         матрицы, расширяет матрицу.
        :param element:
        :return:
        """
        if element is None:
            return self.matrix
        if self.size == 1:
            return self._append_in_base_matrix(self, element)
        if self.size < self.max_size:
            if self.matrix[-2][-1] is not None:
                self._matrix_expanding(self.matrix)
                self._matrix_shift(self.matrix)
                self.size += 1
            self._put_in_matrix(self.matrix, element)
            return self.matrix
        else:
            if self.matrix[self.max_size - 1][self.max_size - 1] is not None:
                raise IndexError
            self._put_in_matrix(self.matrix, element)
            return self.matrix
        return self.matrix

    @classmethod
    def from_iter(cls, iter_obj, max_size=None) -> object:
        """
        Создает матрицу размером max_size, заполняет ее из iter_obj и возвращает заполненную матрицу.
        :param iter_obj:
        :param max_size:
        :return:
        """
        from math import ceil, sqrt
        iter_obj = [i for i in iter_obj if i is not None]
        if not iter_obj:
            m = Matrix(max_size)
            return m
        length = len(iter_obj)
        m = Matrix(max_size)
        size = ceil(sqrt(length))

        if length > m.max_size**2:
            raise IndexError
        elif length > size**2 - size and size < m.max_size:
            m.matrix = [[None for i in range(size+1)] for j in range(size+1)]
            for i, j in m._full_mass_iterator(size+1):
                try:
                    m.matrix[i][j] = iter_obj[0]
                    del iter_obj[0]
                except IndexError:
                    break
            return m
        else:
            m.matrix = [[None for i in range(size)] for j in range(size)]
            for i, j in m._full_mass_iterator(size):
                try:
                    m.matrix[i][j] = iter_obj[0]
                    del iter_obj[0]
                except IndexError:
                    break
            return m


t1 = time.time()
mtrx = Matrix.from_iter(range(1), max_size=2)
t2 = time.time()

print(f'Creation: {t2 - t1}')
print(mtrx)
