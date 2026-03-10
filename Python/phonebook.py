phonebook = {}

def add_new_contact(name, contact_number):
    if name in phonebook.keys():
        phonebook[name].append(contact_number)
        print("Contact added successfully")

    else:
        phonebook[name] = [contact_number]
        print("Contact added successfully")

def search_number(name):
    if name in phonebook:
        print(f"Contact no for user - {name} : {phonebook[name]}")

    else:
        print("Contact does not exist !")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact successfully deleted!")

    else:
        print("Contact does not exist !")


def main():
    print(" Add New Contact\n Search Contact\n Delete contact")

    answer = int(input("Enter Choice :"))

    if answer == 1:
        name = input("Enter Name: ")
        contact_num = int(input("Enter contact number: "))
        add_new_contact(name, contact_num)

    elif answer == 2:
        name = input("Enter Name: ")
        search_number(name)

    elif answer == 3:
        name = input("Enter Name: ")
        delete_contact(name)

while True:
    main()




