from my_slice import my_slice

length = 30
array = list(range(length))
# array = ''.join(map(lambda x: chr(x + 97), range(length)))
limit = range(-length * 2 - 1, length * 2 + 1)

for start in limit:
    for stop in limit:
        for step in limit:
            if step == 0:
                continue
            currect_res = array[slice(start, stop, step)]
            my_res = my_slice(array, start, stop, step)
            assert list(currect_res) == list(my_res)
print('Currect!')