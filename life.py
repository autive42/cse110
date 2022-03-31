with open("life-expectancy.csv") as life_file:
    life_file.readline()
    largest = 0
    smallest = 420

    for line in life_file:
        clean = line.strip()
        parts = clean.split(',')

        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        if life > largest:
            largest = life
        if life < smallest:
            smallest = life
    
    print('The largest life expectancy was {0}. The smallest life expectancy was {1}.'.format(largest, smallest))
