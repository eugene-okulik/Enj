planning_numb = 43

while True:
    user_numb = int(input('Давай сыграем в игру?'))
    if user_numb == planning_numb:
        print('Поздравляю, вы угадали!')
        break
    else:
        print('Попробуйте снова')
