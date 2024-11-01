# SUEDAD, ALQUIN MACABINGUIL BSCS 1-1
# Activity no.2


orders = []
overAllPrice = 0
m, s, p = "", "", 0
# m is main, s is side, p is price
def addOrder(main, side, price):
    order = {"main": main,
             "side": side,
             "price": price}
    orders.append(order)

# this function is to view the orders
def viewOrders():
    overAllPrice = 0
    if not orders:
        print("You have no orders!")
        return
    
    for i, order in enumerate(orders, start = 1):
        print(f"{i}). Main: {order['main']}, Side: {order['side']}, Price: {order['price']}")
        overAllPrice += order["price"]
    print(f"Overall Price is: ₱{overAllPrice}")

# this function is to delete a specific order by using index
def deleteOrder(n):
    if not orders:
        print("No Orders...")
        
    if 1 <= n and n <= len(orders):
        orders.pop(n - 1)
        print("Successfully Deleted..")
    else: 
        print("Invalid input number. Redirecting you in Main Menu..")

# this is the main menu.
def mainMenu():
    print("Welcome to McDo!")
    print("\n McSavers Mix & Match")
    print("Create your Favorite Mix and Match!")

    while True:
        action = input("\n type 'V' to view Orders \n type 'D' to delete orders \n type 'C' to Order \n type 'E' to exit. \n Input Here: \t").lower()
        match action:
            case 'v':
                viewOrders()
            case 'd':
                viewOrders()
                delt = int(input("Enter the number you would like to delete in the cart: "))
                deleteOrder(delt)
            case 'c': # If user inputted "E" the function exits and proceed to the next nested while Loop to start Ordering.
                return
            case 'e': # if user inputted "E" the whole program ends.
                print("\n Thank you for visiting mcDO! \n Exiting program...")
                exit()
            case _:
                print("Invalid Input, Try again.")
                continue


while True:
    mainMenu()
    m , s , p = "", "", 0
    print("Main meals Menu")
    print("\nCombo A ₱79")
    print("1- French Fries")
    print("2- Spaghetti")
    print("3- Burger")

    print("\nCombo B ₱89")
    print("4- Mushroom Pepper Steak")
    print("5- Chicken Fillet")
    print("6- Crispy Chicken Sandwich \n")

    order = int(input("Choose your main: "))
    match order:
        case 1:
            print("You chose French Fries")
            m = "French Fries"
            p = 75
        case 2:
            print("You chose Spaghetti")
            m = "Spaghetti"
            p = 75
        case 3:
            print("You chose Burger")
            m = "Burger"
            p = 75
        case 4:
            print("You chose Mushroom Pepper Steak")
            m = "Mushroom Pepper Steak"
            p = 89
        case 5:
            print("You chose Chicken Fillet")
            m = "Chicken Fillet"
            p = 89
        case 6:
            print("You chose Crispy Chicken Sandwich")
            m = "Crispy Chicken Sandwich"
            p = 89
        case _ :
            print("INVALID MEAL! Redirecting you back..")
            continue 

    while True:

        print(f"You chose {m} as your Main Dish. With a price of ₱{p} \n")
        print(f"Choose a side dish. \n")
        
        print("1- Apple Pie")
        print("2- Sundae (Caramel or Hot Fudge)")
        print("3- Float")
        print("4- Iced Tea")
        print("5- Softdrinks")
        print("6- Iced Coffee Vanilla")
        side = int(input("Choose your side dish: "))
        match side:
            case 1:
                print("You chose Apple Pie")
                s = "Apple Pie"
            case 2:
                print("You chose Sundae")
                s = "Sundae"
            case 3:
                print("You chose Float")
                s = "Float"
            case 4 :
                print("You chose Iced Tea")
                s = "Iced Tea"
            case 5:
                print("You chose Softdrinks")
                s = "Softdrinks"
            case 6:
                print("You chose Iced Coffee Vanilla")
                s = "Iced Coffee Vanilla"
            case _:
                print("INVALID SIDE, Redirecting you back..")
                continue

        print("\n === === === === === === === === === === === === ===")
        print(f"Added {m} as yourMain Dish, and {s} as your Side dish. \n To view and see the total Price of your order(s), type V in the Main Menu. \n Thank you!")
        addOrder(m, s, p)
        input("Input anything here to continue...")
        break