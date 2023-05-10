def vowels_in_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lower_case_word = word.lower()
    result = ''
    for letter in lower_case_word:
        if letter in vowels and letter not in result:
            result += letter + ', '
    return 'Vowels: ' + result[:-2]
