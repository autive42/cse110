kids_meal = float(input("Enter the price of a child's meal: "))
meal = float(input("Enter the price of an adult's meal: "))
child = int(input("Enter the number of children: "))
adult = int(input("Enter the number of adults: "))
tax_rate = float(input("Enter the sales tax rate as a decimal: "))

subtotal = kids_meal * child + meal * adult
print(f"\nSubtotal: {subtotal}")

tax = subtotal * tax_rate
total = tax + subtotal
print(f"Total: {total}")