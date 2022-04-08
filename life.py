with open("life-expectancy.csv") as life_file:
    life_file.readline()
    largest = 0
    smallest = 0

    life = []
    code = []
    year = []
    entity = []

    for line in life_file:
        clean = line.strip()
        parts = clean.split(',')
        
        entity.append(parts[0])
        code.append(parts[1])
        year.append(int(parts[2]))
        life.append(float(parts[3]))
        
        if life[-1] > life[largest]:
            largest = len(life) -1
        if life[-1] < life[smallest]:
            smallest = len(life) -1 
    
    print('The largest life expectancy was {0}. The smallest life expectancy was {1}.'.format(life[largest], life[smallest]))
