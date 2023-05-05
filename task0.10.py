def most_common(letter_1, letter_2):
    lowered_1 = letter_1.lower()
    lowered_2 = letter_2.lower()
    result = ''
    for letter in lowered_2:
        if letter in lowered_1 and letter not in result:
            result += letter + ', '
    if result == '':
        return 'No common letters'
    else:
        return 'Common letters: ' + result[:-2]
