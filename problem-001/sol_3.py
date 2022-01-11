print('\n'.join(__import__('random').sample(open('bh.csv', 'r+').read().splitlines(), int(input('m = ')))))
