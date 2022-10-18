attempt = 0
left = 1
right = 100

print('Загадайте число от 1 до 100: ')
while True:
    try:
        x = (left + right) // 2
        attempt += 1
        answer = input(f'Ваше число {x}? да, больше или меньше?: ')
        if answer == 'да':
            print(f'Я угадал ваше число')
            break
        elif answer == 'больше':
            left = x + 1
        elif answer == 'меньше':
            right = x - 1
        else:
            print('Вводить только: "да", "больше" или "меньше"')
            continue
    except:
        print('Вводить только: "да", "больше" или "меньше"')

print(f'За {attempt} попыток')
with open('result.txt', 'w', encoding="UTF-8") as file:
    file.write(f'Попыток: {attempt}')
