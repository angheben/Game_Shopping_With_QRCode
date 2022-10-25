import pandas as pd
import qrcode


def menu():
    choice = int(input("01) Press one to see the products of the store \n"
                       "02) Press two to add a product in to the shopping cart \n"
                       "03) Press three to see your shopping cart \n"
                       "04) Press four to delete a product of your shopping cart \n"
                       "05) Press five to close your purchase \n"
                       "06) Press six to get out \n"
                       "-> "))
    if choice == 1:
        see_the_products()
    elif choice == 2:
        add_product_shopping_cart()
    elif choice == 3:
        check_shopping_cart()
    elif choice == 4:
        delete_product_shopping_cart()
    elif choice == 5:
        payment()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice, chose again")
        menu()


def see_the_products():
    pass


def add_product_shopping_cart():
    pass


def check_shopping_cart():
    pass


def delete_product_shopping_cart():
    pass


def payment():
    pass


menu()
