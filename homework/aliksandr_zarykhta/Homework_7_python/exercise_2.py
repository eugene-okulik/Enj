words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multiple_words(**kwargs):
    for name_word, count_number in kwargs.items():
        print(name_word * count_number, end='\n')


multiple_words(**words)
