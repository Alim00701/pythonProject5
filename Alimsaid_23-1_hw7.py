def nearest_number(lst, number: int):
    return number, sorted(lst, key=lambda x: abs(x - number))


print(nearest_number([312, 996, 31, 1991], 1000))
print(nearest_number([5, 20.18, 103, 4], 27))


ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(lambda x: x % 2 == 0, ten))
evens = list(map(lambda x: x**2, b))
print(evens)


def ten_d(iter):
    while 1:
        index = input('Enter the index: ')
        if index == 'q':
            print("The program is completed!")
            break
        try:
            index = int(index)
            print(iter[index])
        except IndexError:
            print(f"Вводить только числа! от 0 до {len(ten) -1}, а для выхода нажмите 'q' ")
        except ValueError:
            print(f"Вводите только целые числа от 0 до {len(ten) -1}, а для выходы нажмите 'q' ")


ten_d(ten)
