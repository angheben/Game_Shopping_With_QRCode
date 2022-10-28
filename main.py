import pandas as pd
import qrcode
from pyzbar.pyzbar import decode

df_game_list = pd.DataFrame(pd.read_excel("game_list.xlsx", sheet_name="game_list"))
shopping_cart = {}
list_price = []


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
        qr_code_payment()
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
        print(f"The product {df_game_list.loc[add_shopping_cart]['Product']} has been added to your shopping cart")
        shopping_cart[df_game_list.loc[add_shopping_cart]['ID']] = [df_game_list.loc[add_shopping_cart]['Product'],
                                                                    df_game_list.loc[add_shopping_cart]['Price']]
        menu()


def check_shopping_cart():
    print(shopping_cart)
    menu()


def delete_product_shopping_cart():
    global id_to_delete
    try:
        id_to_delete = int(input("Type the ID of the product that you want to delete of your shopping cart:\n"
                                 "-> "))
    except ValueError as err2:
        print(f"The product of ID {id_to_delete} is not in your shopping cart, try again")
        delete_product_shopping_cart()
    else:
        shopping_cart.pop(id_to_delete)
        menu()


def qr_code_payment():
    for key, values in shopping_cart.items():
        list_price.append(values[1])
    x = sum(list_price)
    print(f'Please, procede with the payment by this appointing your camera to this QR Code')
    data = x
    img = qrcode.QRCode(version=1, box_size=20, border=15)
    img = qrcode.make(data)
    img.save('D:/One Drive/One Drive ANG/OneDrive - ANG/Arquivos '
             'Vitor/curso_de_programacao/conquiste_sua_vaga/gaming_shop_with_QRCode/qrcode_payment.png')
    print("Tks for shopping with us, enjoy your new games :D")
    exit()


menu()
