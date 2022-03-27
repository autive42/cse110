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

    #add item and price to list
    if action == 1:
        cart.append(input("\nWhat item would you like to add? ").capitalize())
        prices.append(float_input("What is the price of the item? "))
        print(f'{cart[-1]} has been added for ${prices[-1]:.2f}')

    elif action == 2:
        print("\nThe items in the shopping cart are:")
        for i in range(len(cart)):
            print(f"{i + 1}. {cart[i]} for ${prices[i]:.2f}")

    #calculate the total
    elif action == 4: 
        total = 0
        for i in prices:
            total += i
        print(f"\nYour total is ${total:.2f}")

    #remove an item
    elif action == 3:
        cartsize = len(cart)
        print("\nSelect an item to remove:")
        for i in range(cartsize):
            print(f"{i + 1}. {cart[i]}")
        selection = int(float_input("Please enter a number (0 to cancel): ")) - 1
        if selection in range(cartsize):
            removed_item = cart.pop(selection)
            prices.pop(selection)
            print(f"\n{removed_item} has been removed.")    
        elif selection < 0:
            print("\nNothing was removed.")
        else:
            print("\nPlease enter a number in the correct range.")

    #quit
    elif action == 5:
        break

    else:
        print("\nPlease enter a number in the correct range.")
