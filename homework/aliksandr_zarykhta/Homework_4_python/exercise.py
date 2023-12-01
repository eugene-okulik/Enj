my_dict = {'tuple': (True, 'Love', 'is', 'Python', 3), 
           'list': ['no', 'like', 'java', 4, 'all'], 
           'dict': {'first': 'of all', 'second': 'war', 'third': 3, 'fourth': 'not four', 'fiveth': 'work days per week'}, 
           'set' :{5, 11, 2000, 'is', 'data', 'of', 'my Birthday'}
           }

#Для того, что хранится под ключом ‘list’: Добавьте в конец списка еще один элемент. Удалите второй элемент списка
my_dict['list'].append('jabascript for me')
my_dict['list'].pop(1)

#Для того, что хранится под ключом ‘dict’: Добавьте элемент с ключом ('i am a tuple',) и любым значением. Удалите какой-нибудь элемент
my_dict['dict']['sixth'] = 'so hard task'
my_dict['dict'].pop('second')

#Для того, что хранится под ключом ‘set’: Добавьте новый элемент в множество. Удалите элемент из множества
my_dict['set'].add(2023)
my_dict['set'].pop()

print('Выведите на экран последний элемент tuple', my_dict['tuple'][ -1])
print('Вывести на экран весь словарь', my_dict)
