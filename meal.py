kids_meal = float(input("Enter the price of a child's meal: $"))
meal = float(input("Enter the price of an adult's meal: $"))
child = int(input("Enter the number of children: "))
adult = int(input("Enter the number of adults: "))
tax_rate = float(input("Enter the sales tax rate as a decimal: "))

subtotal = kids_meal * child + meal * adult
print(f"\nSubtotal: ${subtotal:.2f}")

tax = subtotal * tax_rate
total = tax + subtotal
print(f"Total: ${total:.2f}")

payment = float(input("\nEnter payment amount: $"))
change = payment - total

if payment < total:
    print("\nInsufficient Funds")
else:
    print(f"\nYour change is ${change:.2f}")