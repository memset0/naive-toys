class MySlice:
    def filter(self, index, length, is_add):
        if index < 0:
            index += length
        if is_add:
            if index < 0:
                index = 0
            if index >= length:
                index = length
        else:
            if index < 0:
                index = -1
            if index >= length:
                index = length - 1
        return index

    def __init__(self, iterable, start, stop, step=None):
        length = len(iterable)

        if step == None:
            step = 1
        elif step == 0:
            raise ValueError
        
        if start == None:
            start = 0 if step > 0 else length - 1
        else:
            start = self.filter(start, length, step > 0)
        
        if stop == None:
            stop = length if step > 0 else -1
        else:
            stop = self.filter(stop, length, step > 0)
        
        if step > 0 and start >= stop or step < 0 and start <= stop:
            self._length = 0
        elif step > 0:
            self._length = (stop - start - 1) // step + 1
        else:
            self._length = (stop - start + 1) // step + 1
        
        self._iterable = iterable
        self._start = start
        self._stop = stop
        self._step = step
        self._pointer = None
        # print(start, stop, step, length)

    def __iter__(self):
        self._pointer = self._start
        return self
    
    def __next__(self):
        if self._pointer == None:
            raise ValueError
        if self._step > 0 and self._pointer >= self._stop or self._step < 0 and self._pointer <= self._stop:
            self._pointer = None
            raise StopIteration
        index = self._pointer
        self._pointer += self._step
        return self._iterable[index]

def my_slice(array, start, stop, step):
    return list(MySlice(array, start, stop, step))

if __name__ == '__main__':
    array = "abcde"
    datas = [[1, -3, None], [7, 3, -1], [7, -3, -1], [-7, -4, -1], [-10, -4, -1], [-2, None, None], [None, -2, None]]
    for data in datas:
        currect_res = array[slice(data[0], data[1], data[2])]
        my_res = my_slice(array, data[0], data[1], data[2])
        print(data, ':', currect_res, my_res)
        assert list(currect_res) == list(my_res)