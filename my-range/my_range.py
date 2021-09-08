#!/usr/bin/env python3

class MyRange:

    def __init__(self, start, end=None, step=1):
        if step == 0:
            raise
        if end == None:
            start, end = 0, start
        self._start = start
        self._end = end
        self._step = step
        self._pointer = start
    
    def __getitem__(self, key):
        res = self._start + self._step * key
        if self._step > 0:
            if res >= self._end:
                raise StopIteration
        else:
            if res <= self._end:
                raise StopIteration
        return res
    
    def __iter__(self):
        self._pointer = self._start
        return self
    
    def __next__(self):
        if self._step > 0:
            self._pointer += self._step
            if self._pointer >= self._end:
                raise StopIteration
        else:
            self._pointer += self._step
            if self._pointer <= self._end:
                raise StopIteration
        return self._pointer

if __name__ == '__main__':
    for i in MyRange(10):
        print('range(10):', i)
    t = MyRange(1, -11, -2)
    for i in t:
        print('range(1, -11, -2):', i)
    for i in t:
        print('range(1, -11, -2) again:', i)

# sol #1: using __getitem__
# sol #2: using __next__ && __iter__