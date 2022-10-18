# работа в файле txt
from time import sleep

# file = open('example.txt', 'w', encoding='UTF-8')
# file.write('python programming')
# file.close()
#
# with open('example.txt', 'a', encoding='UTF-8') as file:
#     file.write('\nгиктек ибраимова 103')

with open('example.txt', 'r', encoding='UTF-8') as file:
    for i in file.read():
        sleep(0.2)
        print(i, end='')
    # print(file.read())
    # print(file.readlines()[-2])
    pass
