#create a formatted id badge
'''
first = input('What is your first name?\n').capitalize()

last = input('\nWhat is your last name?\n').upper()

email = input('\nWhat is your email address?\n').lower()

phone = input('\nWhat is your phone number?\n')

title = input('\nWhat is your job?\n').title()

id = input('\nWhat is your ID number?\n')

#uncomment this section and comment above to debug
'''
first = 'Eric'
last = 'HEINER'
email = 'example@email.com'
phone = '(123) 456-7890'
title = "Doin' Your Mom"
id = '420-69'

#format and print the card
print('\nThe ID card is:')
print('-------------------------')
print(f'| {last}, {first}')
print(f'| {title}')
print(f'| ID# {id}\n|')
print(f'| {email}')
print(f'| {phone}')
print('-------------------------')
