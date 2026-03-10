students = {}

def add_students(std_id ,name, age, address, contact):
    if std_id in students:
        print("Student ID already Exists !")

    else:
        students[std_id] = {"name" : name,
                            "age" : age,
                            "address" : address,
                            "contact" : contact}
        print(students)
    return "Student added successfully!"

def update_student(std_id):
    if std_id in students:
        choice = input("What do you want to update? :").lower()
        answer = input(f"Enter {choice} to Update :")
        if choice in students[std_id]:
            students[std_id][choice] = answer

    print(students[std_id])

def add_student_results(std_id):
     if std_id in students:
         maths = int(input("Enter maths results :"))
         art = int(input("Enter art results :"))
         commerce = int(input ("Enter commerce results :"))

         students[std_id]["results"] = {"maths" : maths,
                                        "art" : art,
                                        "commerce" : commerce}
         print("Marks added successfully!")

     else:
        print("invalid student ID!")

def view_student_results(std_id):
    if std_id in students:
        if "results" in students[std_id]:
            for key,val in students[std_id]["results"].items():
                print(f"{key} - {val}")

        else:
            print("No marks available for this student!")

    else:
        print("Student not found!")

def view_student_grades():
    for student_id,student in students.items():
        if "results" in student:
            total_marks = 0

            for mark in student["result"].values():
                total_marks += mark

            if total_marks / len(student["marks"].keys()) > 50:
                print(f"{student["name"]} - Pass")

            else:
                print(f"{student["name"]} - Fail")


def main():
    print("MAIN MENU")
    print("---------")

    print("1)Add Student\n2)Update Student\n3)Add student results\n4)View student results\n5)view grades")

    choice = int(input("enter your choice :"))

    if choice == 1:
        std_id = int(input("Enter student id :"))
        name = input("Enter student name :")
        age = input("Enter student age :")
        address = input("Enter student address :")
        contact = input("Enter student contact :")

        add_students(std_id, name, age, address, contact)

    elif choice == 2:
        std_id = int(input("Enter student id :"))


        update_student(std_id)

    elif choice == 3:
        std_id = int(input("Enter student id :"))

        add_student_results(std_id)

    elif choice == 4:
        std_id = int(input("Enter student id to view results :"))

        view_student_results(std_id)

    elif choice == 5:
        std_id = int(input("Enter student id to view grades :"))

        view_student_grades()

    else:
        quit
while True:
    main()
