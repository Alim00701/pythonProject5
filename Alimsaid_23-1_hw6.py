def even_odd(number):
    if type(number) is not int:
        return None
    elif number % 2 == 0:
        return True
    else:
        return False


print(even_odd(4))


def spelling_at_minimum(sentence):
    if sentence[0].isupper() and sentence[-1] == '.':
        return sentence
    else:
        print('Начинать только с заглавной буквой и заканчивать точкой!')


print(spelling_at_minimum('Привет.'))


def average(*args):
    return sum(args) // len(args)


print(average(3, 3, 3))


def nearest_number(lst, number: int):
    a = [abs(i - number) for i in lst]
    b = a.index(min(a))
    return f'({lst}, {number} == {lst[b]})'


print(nearest_number([65, 34, 89.56, 564, 93], 86))
