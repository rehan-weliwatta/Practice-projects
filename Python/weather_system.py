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

    while choice:
        if choice == 1:
            for i in range(3):
                day_of_week = int(input("Enter a day 1-7 (or 0 to exit to menu):"))

                print("1)Morning \n2)Day\n3)Night")

                time_of_day = int(input("Enter your choice 1-3 (or 0 to exit to menu):"))
                temperature = float(input("Enter temperature (or 0 to exit to menu):"))

                if temps_for_a_week_per_day[day_of_week -1] :
                    for days_of_week in temps_for_a_week_per_day:
                        days_of_week[time_of_day-1] = temperature
                        print(temps_for_a_week_per_day)
                        break




        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 0:
            quit()

        else:
            print("Invalid input!")

