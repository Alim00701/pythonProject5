letters = 'аоуиыэеёюяaeiouy'
while True:
    sogl, glas = 0, 0
    word = input('Введите слово: ')

    if word == 'q':
        print('Программа завершена')

    for i in word.lower():
        if i in letters:
            glas += 1
        else:
            sogl += 1

    glas_proc = round(glas / len(word) * 100, 2)
    sogl_proc = round(sogl / len(word) * 100, 2)

    print(f'Слово: {word}\n'
          f'Количество буквы: {len(word)}\n'
          f'Согласные буквы: {sogl}\n'
          f'Гласные буквы: {glas}\n'
          f'Согласные/Гласные: {glas_proc}%, {sogl_proc}%'
