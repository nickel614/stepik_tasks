import time
class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.max_size = max_size if max_size else Matrix.MAX_SIZE
        self.matrix = [[None]]
        self.size = len(self.matrix)

    def __str__(self):
        s = ''
        for i in self.matrix:
            for j in i: s += f'{j} '
            s = s[:len(s) - 1]
            s += '\n'
        return s

    def pop(self): #метод возвращает удаленный элемент из матрицы, находящийся в ее конце
        if self.size == 1:
            raise IndexError
        m = self.matrix
        def full_mass_iterator(size):
            for i in range(size):
                for j in range(size): yield i, j

        def matrix_deexpanding(self):
            m1 = []
            for i, j in full_mass_iterator(self.size):
                if self.matrix[i][j] == None:
                    self.size -= 1
                    break
                m1.append(self.matrix[i][j])
            self.matrix = [[None for j in range(self.size)] for i in range(self.size)]
            for i, j in full_mass_iterator(self.size):
                try:
                    self.matrix[i][j] = m1.pop(0)
                except:
                    return self.matrix

        prev, i1, j1 = None, 0, 0
        for i, j in full_mass_iterator(self.size):
            if prev != None and m[i][j] == None:
                popped = prev
                m[i1][j1] = None
                if i * self.size + j == (self.size - 1) ** 2 - (self.size - 1) + 1:
                    m = matrix_deexpanding(self)
                return popped
            prev = m[i][j]
            i1 = i
            j1 = j

    def append(self, element=None):
        def matrix_expanding(m):
            size = len(m)
            m.append([])
            for i in range(size): m[len(m) - 1].append(None)
            for i in range(len(m)): m[i].append(None)
            return m

        def matrix_shift(m):
            size = len(m)
            for i in range(len(m) - 1)[:size - 1]:
                nones = m[i].count(None)
                for j in range(nones): m[i].remove(None)
                for j in range(nones): m[i].append(m[i + 1][j])
                for j in range(nones):
                    m[i + 1].pop(0)
                    m[i + 1].append(None)
            return m

        if element == None: return self.matrix

        if len(self.matrix) == 1:
            self.matrix[0][0] = element
            self.matrix = matrix_expanding(self.matrix)
            self.matrix = matrix_shift(self.matrix)
            self.size += 1
            return self.matrix

        if len(self.matrix) < self.max_size:
            size = len(self.matrix)
            if self.matrix[-2][-1] != None:
                self.matrix = matrix_expanding(self.matrix)
                self.matrix = matrix_shift(self.matrix)
                self.size += 1
                size += 1
            for i in range(size):
                for j in range(size):
                    if self.matrix[i][j] == None:
                        self.matrix[i][j] = element
                        return self.matrix
        else:
            if self.matrix[self.max_size - 1][self.max_size - 1] != None: raise IndexError
            for i1, i in enumerate(iterable=self.matrix):
                for j1, j in enumerate(iterable=i):
                    if self.matrix[i1][j1] == None:
                        self.matrix[i1][j1] = element
                        return self.matrix
        return self.matrix

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        try: iter(iter_obj)
        except: raise TypeError

        m = Matrix(max_size)
        for i in iter_obj:
            m.append(i)
        return m




mtrx = Matrix(3)

t1 = time.time()

mtrx.append(1)

t2 = time.time()

mtrx.append()

t3 = time.time()

print(f'appending: {t2 - t1}')
print(f'popping: {t3 - t2}')
