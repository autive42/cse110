#generate a timetable for inputed number

#number = int(input("Calculate a timetable up to what number? "))
number = 5
digits = len(str(number ** 2))

for r in range(1, number + 1):
    for c in range (1, number + 1):
        print(f'{r * c:{digits}}', end='  ')
    print()
