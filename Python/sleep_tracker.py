hours_of_sleep = []

while True:
    print("----------| MENU |-----------")
    print("1)Add hour of sleep\n2)View Average sleep\n3)View days that exceeds 8hours of sleep")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        for hour in range(7):
            sleep_hours = int(input("Enter the hours of sleep :"))
            hours_of_sleep.append(sleep_hours)

    elif choice == 2:
        print(f"You had an average sleep of {sum(hours_of_sleep) // 7} hours this week!")

    elif choice == 3:
        counter = 0
        for i in hours_of_sleep:
            if i > 8 :
                counter += 1
        print(f"You have got more than 8 hours sleep for {counter} days! ")

