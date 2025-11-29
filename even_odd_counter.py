even_numbers = 0
odd_numbers = 0

for number in range(0 , 101):
    if number & 1:
        odd_numbers += 1

    else:
        even_numbers += 1


print(f"Even Numbers :{even_numbers} , Odd numbers : {odd_numbers}")


numbers = []

while True:
    number = int(input("Enter a number (or enter 0 to exit):"))

    if number != 0:
        numbers.append(number)

    else:
        print(sum(numbers))
        break



