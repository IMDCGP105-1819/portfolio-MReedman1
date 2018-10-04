name = input('Enter your Name:')
age = int(input('Enter your Age:'))
height = int(input('Enter your Height (specify inches):'))
weight = int(input('Enter your Weight  (specify kilograms):'))
eyes = input('Enter your Eye colour:')
hair = input('Enter your Hair colour:')

print(f"Let's talk about {name}.")
print(f"He is this {age} year old.")
if age > 1 and age < 13:
    print('This person is a child')
elif age >= 13 and age < 18:
    print('This person is a teenager.')
elif age >= 18:
    print('The person is an adult.')
else:
    print('check that your input is an integer and try again')
print(f"You are {height} inches tall.")
if height <= 66:
    print('Midget')
elif height > 66 and height < 72:
    print('Normal height')
elif height >= 72 and height < 77:
    print('Tall')
elif height >=77:
    print('Giant')
print(f"He's {weight} pounds heavy.")
if weight <= 75:
    print('You are Underweight')
elif weight > 75 and weight < 100:
    print('You are at a Healthy weight')
elif weight >= 100 and weight < 120:
    print('You are Overweight')
elif weight >= 120 and weight < 160:
    print('You are Obese')
elif weight >=160:
    print('Very Obese')
print(f"He's got {eyes} eyes and {hair} hair.")
