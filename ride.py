minage = 18
minheight = 62
def ride():
    print('\nYou may ride.')
def noride():
    print('\nYou may not ride.')

age1 = float(input('What is the age of the first rider? '))
height1 = float(input('What is the height of the first rider? '))

while second not in ('y','n',):
    second = input('Is there a second rider? (y/n) ').lower()

if second == 'y':
    age2 = float(input('What is the age of the second rider? '))
    height2 = float(input('What is the height of the second rider? '))
else:
    age2 = minage
    height2 = minheight

if age1 < 36 or age2 < 36:
    noride()
elif second == 'n':
    if age1 < 18 or height1 < 62:
        noride()
    else:
        ride()
else:
    if age1 < 18 and age2 < 18:
        if age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
            ride()
        else:
            noride()
    else:
        ride()
