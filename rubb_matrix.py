class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        if max_size: self.max_size = max_size
        else: self.max_size = self.MAX_SIZE
        self.matrix = [[None]]

    def __str__(self):
        s = ''
        for i in self.matrix:
            for j in i: s += f'{j} '
            s = s[:len(s) - 1]
            s += '\n'
        return s

    def matrix_expanding(self, m):
        size = len(m)
        m.append([])
        for i in range(size): m[len(m) - 1].append(None)
        for i in range(len(m)): m[i].append(None)
        return m

    def matrix_shift(self, m):
        size = len(m)
        for i in range(len(m) - 1)[:size - 1]:
            nones = m[i].count(None)
            for j in range(nones): m[i].remove(None)
            for j in range(nones): m[i].append(m[i + 1][j])
            for j in range(nones):
                m[i + 1].pop(0)
                m[i + 1].append(None)
        return m

    def append(self, element=None):
        if element == None: return self.matrix

        if len(self.matrix) == 1: # обработка единичной матрицы
            self.matrix[0][0] = element
            self.matrix_expanding(self.matrix)
            self.matrix_shift(self.matrix)
            return self.matrix

        if len(self.matrix) < self.max_size: # контроль
            size = len(self.matrix)
            if self.matrix[-2][-1] != None:
                self.matrix_expanding(self.matrix)
                self.matrix_shift(self.matrix)
                size += 1
            for i in range(size):
                for j in range(size):
                    if self.matrix[i][j] == None:
                        self.matrix[i][j] = element
                        return self.matrix
        else:
            if self.matrix[self.max_size-1][self.max_size-1] != None: raise IndexError
            for i1, i in enumerate(iterable=self.matrix):
                for j1, j in enumerate(iterable=i):
                    if self.matrix[i1][j1] == None:
                        self.matrix[i1][j1] = element
                        return self.matrix
        return self.matrix

    def pop(self):
        size = len(self.matrix)
        def mass_iterator(size):
            for i in range(size - 1):
                for j in range(size): yield i, j

        def full_mass_iterator(size):
            for i in range(size):
                for j in range(size): yield i, j

        def matrix_deexpanding(m):
            m1 = []
            for i, j in full_mass_iterator(size):
                if m[i][j] == None:
                    break
                m1.append(m[i][j])
            m = [[None for j in range(size - 1)] for i in range(size - 1)]
            for i, j in full_mass_iterator(size - 1):
                try:
                    m[i][j] = m1.pop(0)
                except:
                    return m

        def pop(m):
            prev, i1, j1 = None, 0, 0
            for i, j in full_mass_iterator(size):
                if prev != None and m[i][j] == None:
                    popped = prev
                    m[i1][j1] = None
                    if i * size + j == (size - 1) ** 2 - (size - 1) + 1:
                        m = matrix_deexpanding(m)
                        pass
                    return m
                prev = m[i][j]
                i1 = i
                j1 = j



    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        pass

matrix = Matrix()
print(type(matrix))
print(matrix)
for i in range(1, 4):
    matrix.append(i)
    print(matrix)
    print('*' * 10)
