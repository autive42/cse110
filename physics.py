import math

mass = float(input('Mass in kg: '))
gravity = float(input('Gravity in m/s^2 (9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time in seconds: '))
density = float(input('Density of the fluid in kg/m^3 (1.3 for air, 1000 for water): '))
area = float(input('Cross sectional area in m^2: '))
drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

'''
#debug
mass = 5
gravity = 9.8
time = 10
density = 1.3
area = 0.01
drag = 0.55
'''

c = 0.5 * density * area * drag
velocity = math.sqrt(mass * gravity  / c) * (1 - math.exp(-math.sqrt(mass * gravity * c)/mass * time))

print(f'\nThe inner value of c is {c:.3f}')
print(f'The velocity after {time:.1f} is {velocity:.3f}')