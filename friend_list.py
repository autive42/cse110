friends = []

while True:
    item = input("Type the name of a friend (q to exit): ")
    if item != 'q':
        friends.append(item.capitalize())
    else:
        break

print("Your friends are:")
for i in friends:
    print(i)
