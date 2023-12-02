my_dict = {'tuple': (True, 'Love', 'is', 'Python', 3),
           'list': ['no', 'like', 'java', 4, 'all'],
           'dict': {'first': 'of all', 'second': 'war', 'third': 3,
                    'fourth': 'not four', 'fiveth': 'work days per week'},
           'set': {5, 11, 2000, 'is', 'data', 'of', 'my Birthday'}
           }

my_dict['list'].append('jabascript for me')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'set with one element'
my_dict['dict'].pop('second')

my_dict['set'].add(2023)
my_dict['set'].pop()

print('Выведите на экран последний элемент tuple', my_dict['tuple'][-1])
print('Вывести на экран весь словарь', my_dict)
