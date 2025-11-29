
c0 = int(input("Enter non-negative or non-zero number :"))
counter = 0
if c0 > 0 :
    while c0 != 1:

        counter += 1

        if c0 % 2 == 0:
            c0 //=  2

        else:
            c0 = 3 * c0 + 1

    print(f"Steps :{counter}")
else:
    print("Enter a non-negative or non-zero number")



