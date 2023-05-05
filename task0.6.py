def maximum(*numbers):
    maximum_number = numbers[0]
    for element in range(1, len(numbers)):
        if numbers[element] > maximum_number:
            maximum_number = numbers[element]
    return maximum_number
