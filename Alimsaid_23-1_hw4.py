data_tuple = ('h', 6.13, 'c', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'G')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    elif data_tuple != str:
        numbers.append(i)

numbers.remove(6.13)
numbers.insert(1, 2)
numbers.sort()
d = numbers.pop(0)
letters.append(d)
numbers = [i * i for i in numbers]
letters.reverse()
letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)
print(f'letters: {letters_tuple}')
print(f'numbers: {numbers_tuple}')
