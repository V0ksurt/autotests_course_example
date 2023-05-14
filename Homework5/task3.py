# Котики и их человеки
# В зоомагазине "Всё для вашей киски" есть книга о котах и покупателях - cats_data.
# Данные о кошках и их владельцах записаны списком кортежей,
# где каждый кортеж состоит из: Кличка котика, Возраст котика, Имя покупателя, Фамилия покупателя.
# Имена некоторых владельцев повторяются, потому что у них несколько кошек.
# Необходимо оптимизировать хранение данных таким образом, чтобы для каждого владельца при выводе (одна строка)
# данные о всех его животных отображались в одной строке, на новой строке следующий покупатель и все его питомцы и т.д.
# Формат для одного покупателя:
# Имя_покупателя Фамилия_покупателя: Кличка_котика1, Возраст; ...; Кличка_котикаN, Возраст\n
# Например (Ввод --> Вывод):
# Ввод
# [('Мартин', 5, 'Алексей', 'Егоров'),
#  ('Фродо', 3, 'Анна', 'Самохина'),
#  ('Вася', 4, 'Алексей', 'Егоров')]
# Вывод
# Алексей Егоров: Мартин, 5; Вася, 4
# Анна Самохина: Фродо, 3
#


def everything_for_your_cat(cats_data):
    """
    Оптимизирируем хранение данных таким образом, чтобы для каждого владельца данные о всех его животных отображались в
    одной строке, а на новой строке следующий покупатель и все его питомцы
    :param cats_data: Список кортежей данных о кошках и их владельцах
    :return: Строка с именем владельца и всех его питомцев
    """
    our_str = ''
    for index_one in range(len(cats_data)):
        if cats_data[index_one][2] and cats_data[index_one][3] in our_str:
            continue
        our_str += f'{cats_data[index_one][2]} {cats_data[index_one][3]}: ' \
                   f'{cats_data[index_one][0]}, {cats_data[index_one][1]}'
        for index_next_pets in range(index_one + 1, len(cats_data)):
            if cats_data[index_next_pets][2:] == cats_data[index_one][2:]:
                our_str += f'; {cats_data[index_next_pets][0]}, {cats_data[index_next_pets][1]}'
        our_str += '\n'
    return our_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [[('Мартин', 5, 'Алексей', 'Егоров'),
         ('Фродо', 3, 'Анна', 'Самохина'),
         ('Вася', 4, 'Алексей', 'Егоров')],
        [('Мартин', 5, 'Алексей', 'Егоров'),
         ('Фродо', 3, 'Анна', 'Самохина'),
         ('Вася', 4, 'Андрей', 'Белов'),
         ('Муся', 7, 'Игорь', 'Бероев'),
         ('Изольда', 2, 'Игорь', 'Бероев'),
         ('Снейп', 1, 'Марина', 'Апраксина'),
         ('Лютик', 4, 'Виталий', 'Соломин'),
         ('Снежок', 3, 'Марина', 'Апраксина'),
         ('Марта', 5, 'Сергей', 'Колесников'),
         ('Буся', 12, 'Алена', 'Федорова'),
         ('Джонни', 10, 'Игорь', 'Андропов'),
         ('Мурзик', 1, 'Даниил', 'Невзоров'),
         ('Барсик', 2, 'Виталий', 'Соломин'),
         ('Рыжик', 7, 'Владимир', 'Медведев'),
         ('Матильда', 8, 'Андрей', 'Белов'),
         ('Гарфилд', 3, 'Александр', 'Березуев')],
        [('Мартин', 5, 'Алексей', 'Егоров'),
         ('Фродо', 3, 'Анна', 'Самохина'),
         ('Вася', 4, 'Андрей', 'Белов'),
         ('Муся', 7, 'Игорь', 'Бероев'),
         ('Изольда', 2, 'Игорь', 'Бероев'),
         ('Снейп', 1, 'Игорь', 'Бероев'),
         ('Лютик', 4, 'Игорь', 'Бероев'),
         ('Снежок', 3, 'Игорь', 'Бероев'),
         ('Марта', 5, 'Андрей', 'Белов'),
         ('Буся', 12, 'Анна', 'Самохина'),
         ('Джонни', 10, 'Андрей', 'Белов'),
         ('Мурзик', 1, 'Алексей', 'Егоров'),
         ('Барсик', 2, 'Андрей', 'Белов'),
         ('Рыжик', 7, 'Анна', 'Самохина'),
         ('Матильда', 8, 'Андрей', 'Белов'),
         ('Гарфилд', 3, 'Алексей', 'Егоров')],
        [], [('Гарфилд', 3, 'Алексей', 'Егоров')]
        ]

test_data = ['''Алексей Егоров: Мартин, 5; Вася, 4
Анна Самохина: Фродо, 3
''',
             '''Алексей Егоров: Мартин, 5
Анна Самохина: Фродо, 3
Андрей Белов: Вася, 4; Матильда, 8
Игорь Бероев: Муся, 7; Изольда, 2
Марина Апраксина: Снейп, 1; Снежок, 3
Виталий Соломин: Лютик, 4; Барсик, 2
Сергей Колесников: Марта, 5
Алена Федорова: Буся, 12
Игорь Андропов: Джонни, 10
Даниил Невзоров: Мурзик, 1
Владимир Медведев: Рыжик, 7
Александр Березуев: Гарфилд, 3
''',
             '''Алексей Егоров: Мартин, 5; Мурзик, 1; Гарфилд, 3
Анна Самохина: Фродо, 3; Буся, 12; Рыжик, 7
Андрей Белов: Вася, 4; Марта, 5; Джонни, 10; Барсик, 2; Матильда, 8
Игорь Бероев: Муся, 7; Изольда, 2; Снейп, 1; Лютик, 4; Снежок, 3
''', '', '''Алексей Егоров: Гарфилд, 3
''']

for i, d in enumerate(data):
    assert everything_for_your_cat(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')