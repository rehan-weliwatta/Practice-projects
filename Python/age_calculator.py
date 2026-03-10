def classify_age(age):
    if age < 13:
        return "child"

    elif 13 < age < 18 :
        return "Teen"

    elif 18 < age < 50:
        return "Adult"

    return "Senior Citizen"


def main():
    current_year = int(input("Enter the current year :"))
    birth_year = int(input("Enter birth year :"))
    age = current_year - birth_year

    classify_age(age)

main()


