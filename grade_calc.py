grade = float(input('Enter your grade: '))
print(grade)

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
else:
    letter = 'F'

grade_last = grade % 10

sign = ''
if grade_last >= 7:
    sign = '+'
elif grade_last < 3:
    sign = '-'

if letter == 'F':
    sign = ''

print(f'\nYour final grade is {letter}{sign}.')

if grade >= 70:
    print('Congratulations on passing!')
else:
    print('Better luck next time')
