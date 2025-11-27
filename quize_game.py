print("Welcome to the Quiz")

playing = int(input("Enter number 1 to play (or enter number 0 to exit) :"))

if playing == 0:
    print("Quiting......")
    quit()

elif playing == 1:
    print("Game Starting......")
    print("-------------------")

    answer = input("What is the main commercial city of Sri Lanka? ").lower()
    if answer != "colombo":
        print("Wrong ! It's Colombo !!")
        quit()

    else:
        print("Correct answer!")
        print("-------------------")
        answer = input("What is the color of sky? ").lower()

        if answer != "blue":
            print("Wrong ! It's Blue!!")
            quit()
        else:
            print("Correct answer! You Win !")
            print("-------------------")
else:
    print("Invalid input!")