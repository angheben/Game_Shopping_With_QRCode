import pandas as pd
import qrcode_test

df_game_list = pd.DataFrame(pd.read_excel("game_list.xlsx", sheet_name="game_list"))
shopping_cart = []
price_shopping_cart = []


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
    print(df_game_list)
    menu()


def add_product_shopping_cart():
    global add_shopping_cart
    try:
        add_shopping_cart = int(input("Select the ID of the product that you want to add at your shopping cart\n"
                                      "-> "))
    except ValueError as err1:
        print("ID not found, please try again")
        add_product_shopping_cart()
    else:
        print(f"The product {df_game_list[add_shopping_cart]['Product']} has been added to your shopping cart")
        shopping_cart.append(df_game_list[add_shopping_cart]['Product'])
        print(shopping_cart)
        menu()


def check_shopping_cart():
    print(pd.DataFrame(shopping_cart))


def delete_product_shopping_cart():
    global id_to_delete
    try:
        id_to_delete = int(input("Type the ID of the product that you want to delete of your shopping cart:\n"
                                 "-> "))
    except ValueError as err2:
        print(f"The product of ID {id_to_delete} is not in your shopping cart, try again")
        delete_product_shopping_cart()
    else:
        shopping_cart.remove(id_to_delete)
        menu()


def payment():

    # Learn how to put the price of the spreadsheet in a QR Code

    pass


menu()
