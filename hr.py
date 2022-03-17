with open("hr_system.txt") as file:
    for line in file:
        parts = line.split(' ', 4)
        pay = int(parts[3]) / 24
        if parts[2].lower() == 'engineer':
            pay += 1000
        print('{0} (ID: {1}), {2} - ${3:.2f}'.format(parts[0], parts[1], parts[2], pay))
