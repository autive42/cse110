#force float data type 
def float_input(message):
    while True:
        try:
            inp = float(input(message))
            return inp
            break
        except:
            print("\nPlease enter a number.")

cart = []
prices = []

while True:
    action = int(float_input("\nPlease Select one:\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\n(1-5): "))
    if action == 1:
        #add item to list
        cart.append(input("What item would you like to add? ").capitalize())
        #prices.append(float_input("What is the price of the item? "))
    elif action == 2:
        print("The items in the shopping cart are:")
        for i in cart:
            print(i)
    elif action == 3 or action == 4:
        print("\nThis action has not been configured yet")
    elif action == 5:
        break
    else:
        print("\nPlease enter a number in the correct range.")
