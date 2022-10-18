menu = {
    'borsh' : {'капуста', 'свекла', 'мясо'},
    'venegret' : ['свекла', 'картошка', 'морковь']
}

left = 1
right = 100
while True:
    current = (left+right)//2
    is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
    if is_right.lower() == 'да':
        print('Я его угадал!')
        break
    elif is_right=='больше':
        left = current + 1
    else:
        right = current - 1

#
# print(borsh.union(venegret))
#
# print(borsh.intersection(venegret))
# print(borsh & venegret)


# a = dict('python') - слова

# lst = [1, 2, 3, 1, 2, 4]
# set1 = {1, 2, 3, 1, 2, 4}
#
# set1.remove(2)
# set1.add('qwerty')
# print(lst)
# print(type(set1))
#
#
# student_2 = dict(name='alice', age=18, height=175, car='lexus 570')
# print(student_2)
#
# student = {
#     'name': 'Adilet',
#     'age': 19,
#     'height': 1.78,
#     'hobby': ['chess', 'english', 'programming'],
#     'married': False,
#     'parents+code': ('279865', '312859'),
#     'rates': {1: 'отлично', 2: 'хорошо', 3: 'отлично'}
# }
#
# # добавление
# student['knowledge'] = ['cook', 'drive']
# student.update(student_2)
# student['hobby'].append('boxing')
#
# # изменение
# student['age'] += 1
#
# # удаление
# del student['rates']
# student['hobby'].remove('chess')
# # hobby = student.pop('hobby')
#
# print(student)
#
# new_student = student
#
# new_student['name'] = 'samat'
# print(new_student)
