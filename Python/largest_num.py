

numbers = [1, 2, 10, 5, 6]

if numbers:
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number

    print(max_num)

else:
    print("No numbers found")



