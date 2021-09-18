# AUTHOR: whisperain (https://github.com/memset0)

from my_array import Array

STEP = 1.5

class List:
    def __len__(self):
        return self.len

    def __getitem__(self, index):
        return self.arr[index if index >= 0 else index + self.len]

    def __setitem__(self, index, value):
        self.arr[index if index >= 0 else index + self.len] = value

    def __delitem__(self, index):
        for i in range(index, self.len - 1):
            self.arr[i] = self.arr[i + 1]
        self.len -= 1

    def __str__(self):
        return str(self._list())

    def _list(self):
        return [self.__getitem__(i) for i in range(self.len)]

    def _malloc(self, inneed):
        if inneed > self.lim:
            data = self._list()
            self.lim = int(inneed * STEP)
            del self.arr
            self.arr = Array(self.lim)
            for i in range(self.len):
                self.arr[i] = data[i]

    def append(self, value):
        self._malloc(self.len + 1)
        self.arr[self.len] = value
        self.len += 1

    def pop(self, index=-1):
        if index == -1:
            self.len -= 1
            return self.arr[self.len]
        else:
            result = self.arr[index]
            for i in range(index, self.len - 1):
                self.arr[i] = self.arr[i + 1]
            return result

    def extend(self, iterables):
        source = [item for item in iterables]
        self._malloc(self.len + len(source))
        for value in source:
            self.arr[self.len] = value
            self.len += 1

    def index(self, value, start=None, end=None):
        start = 0 if start == None else start
        end = self.len if end == None else end
        for i in range(start, end):
            if self.arr[i] == value:
                return i
        raise ValueError(str(value) + ' is not in list')

    def insert(self, index, value):
        self._malloc(self.len + 1)
        for i in range(self.len - 1, index, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index] = value

    def remove(self, value):
        for i in range(self.len):
            if self.arr[i] == value:
                while i < self.len:
                    self.arr[i] = self.arr[i + 1]
                    i += 1
                self.len -= 1

    def reverse(self):
        for i in range(self.len // 2):
            temp = self.arr[i]
            self.arr[i] = self.arr[self.len - 1 - i]
            self.arr[self.len - 1 - i] = temp

    def __init__(self, iterables=None):
        if iterables == None:
            source = []
        else:
            source = [item for item in iterables]
        self.len = len(source)
        self.lim = self.len
        self.arr = Array(self.len)
        for i in range(self.len):
            self.arr[i] = source[i]
