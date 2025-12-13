#temps_for_a_week_per_day = []

'''for i in range(7):
    temps = []
    for j in range(3):
        temps.append(0.0)

        temps_for_a_week_per_day.append(temps)

print(temps_for_a_week_per_day)'''

temps_for_a_week_per_day = [[0.0 for i in range(3)] for i in range (7)]

while True:
    print("---------| Menu |----------")
    print("1)Add temperature \n2)view temperature\n3)Get average temperature")

    choice = int(input("Enter your choice 1-3 (or 0 to quit):"))

    if choice == 1:
        day_of_week = int(input("Enter a day 1-7 :"))

        if day_of_week in range(1,8):
            print("1)Morning \n2)Day\n3)Night")

            time_of_day = int(input("Enter your choice 1-3 :"))

            if time_of_day in range(1,4):
                temperature = float(input("Enter temperature :"))

                temps_for_a_week_per_day[day_of_week - 1][time_of_day - 1] = temperature

            else:
                print("Enter a valid hour!")

        else:
            print("Enter valid date!")

    elif choice == 2:
        day_of_week = int(input("Enter a day 1-7 :"))

        if day_of_week in range(1, 8):
            print(f"Your temperature for the day is : {temps_for_a_week_per_day[day_of_week - 1][time_of_day - 1]}")

        else:
            print("Enter valid date!")

    elif choice == 3:
        day_of_week = int(input("Enter a day 1-7 :"))

        if day_of_week in range(1, 8):
            print(f"Average temperature for the given day : {sum(temps_for_a_week_per_day[day_of_week - 1]) / 3}")

    elif choice == 4:
        total = 0
        for day in temps_for_a_week_per_day:
            for temp in day:
                total += temp
        print(f"Average temperature of the week : {total/21}")

    elif choice == 0:
        quit()

    else:
        print("Invalid input!")

