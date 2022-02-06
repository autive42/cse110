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

print(f"\nYou're grade is {letter}.")

if grade >= 70:
    print('Congratulations on passing!')
else:
    print('Better luck next time')
