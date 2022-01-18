name = input('Enter your name:')

color = input('Hello ' + name + '. Enter your favorite color:')

#if color == 'Purple' or color == 'purple':
if color.capitalize() == 'Purple':
    print('Nice')
else:
    print('What a dumb color')
