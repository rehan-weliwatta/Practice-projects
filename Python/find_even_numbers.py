def find_even_numbers(numbers):

    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

    '''return [number for number in  numbers if number % 2 == 0] same thing using list comprehension'''


numbers_list = [i for i in range(1,21)]
