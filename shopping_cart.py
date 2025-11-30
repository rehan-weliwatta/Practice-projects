import time

cart = []

products = ['suger' , 'biscuit' , 'milk' , 'oil' , 'rice']

while True:
    print("                                                    ")
    print("                                                    ")
    print("----------------Grocery Store-----------------------")
    print("----------------| Main Menu |-----------------------")
    print("             1)View available products \n"
          "             2)View Cart \n"
          "             3)Remove items from cart \n"
          "             4)Quit")

    answer = input("Enter your choice :")

    if answer == "1":
        print("---------------| Available Products |---------------")

        for product in products:
            print(product)

        print("                                                     ")
        print("                                                     ")

        answer = input("1.Add products to cart(or enter 0 to go back):")

        while answer == "1":
            add_product = input("Enter product name to add (or enter 0 to go back):").lower()

            if add_product in products:
                cart.append(add_product)

            elif add_product == "0":
                print("Items added to cart successfully")
                time.sleep(10)
                break

            else:
                print("Invalid input!")

    if answer == "2":
        print("-----------------| Your cart |-----------------")
        for cart_items in cart:
            print(cart_items)

        print("                                                    ")
        print("1.Remove Items from cart")
        print("2.Clear cart")

        answer = input("Enter 1 or 2 (Enter 0 to exit) :")

        while answer == '1':
            remove_item = input("Enter item name to remove (or enter 0 to exit):").lower()

            if remove_item in cart:
                cart.remove(remove_item)

            elif remove_item == "0":
                break

            else:
                print("Invalid item")

        if answer == '2':
            cart.clear()
            print("Cart cleared successfully")
            pass

        elif answer == "0":
            pass
