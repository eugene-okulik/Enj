text_task = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
    Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

text_task = text_task.replace(',', 'ing,')
text_task = text_task.replace('.', 'ing.')
modified_text = text_task.split()
for word in modified_text:
    if 'ing' in word:
        print(word, end=' ')
    else:
        print(word + 'ing', end=' ')
