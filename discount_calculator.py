while True :
    is_member = input("Are You a Member (yes / no) :").lower() == "yes"
    bill_value = int(input("Enter Your Bill Value :"))
    coupon = input("Are you using a coupon (yes / no) :").lower() == "no"
    vegetables = input("Are you buying vegetables (yes / no) :").lower() == "yes"
    discount = bill_value / 100 * 20

    if is_member and bill_value > 5000 and coupon and vegetables :
        print(f"Bill Value :{bill_value}")
        print(f"Total discount :{discount}")
        print("----------------------------------------")
        print(f"Total bill after discount :{bill_value - discount}")

    else:
        print("You are not eligible for the discount!")