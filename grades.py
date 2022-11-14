keepAsking = True


while keepAsking is True:
    try:
        score = int(input('Enter your score: '))
        outOf = int(input('Enter perfect score: '))
    except:
        print('Please enter a valid score.')
        exit()

    divOutOfBy5 = outOf / 5
    dividend = score / divOutOfBy5
    final = 0
    if dividend >= 5:
        final = '1, good job!'
    elif dividend >= 4:
        final = '2, very close to perfect!'
    elif dividend >= 3:
        final = '3, you could\'ve done better!'
    elif dividend >= 2:
        final = '4, nope, you\'re not studying!'
    else:
        final = '5, I\'m disappointed.'

    print(final)
    answer = input('Use the program again? (y/n)\n').lower()
    if answer == 'n':
        keepAsking = False
        print('Come back again!')