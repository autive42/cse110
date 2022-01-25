print('Please enter the following:')

#user input
adj = input('\nadjective:').lower()
animal = input('\nanimal:').lower()
exclamation = input('\nexclamation:').capitalize()
verb1 = input('\nverb:').lower()
verb2 = input('\nverb:').lower()

#debug
'''
adj = 'happy'
animal = 'zebra'
exclamation = 'HOORAY'
verb1 = 'read'
verb2 = 'drive'
'''

#print result
print('\n\nYour story is:\n')

print('The other day, I was really in trouble. It all started when')
print(f'I saw a very {adj} {animal} {verb1} down the hallway.')
print(f'"{exclamation}!" I yelled. But all I could think to do was to')
print(f'{verb1} over and over. Miraculously, that caused it to stop,')
print(f'but not before it tried to {verb2} right in front of my family.')
