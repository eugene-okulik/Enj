text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
    Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

text = text.replace(',', 'ing,')
text = text.replace('.', 'ing.')
modified_text = text.split()
for word in modified_text:
    if 'ing' in word:
        print(word, end=' ')
    else:
        print(word + 'ing', end=' ')
