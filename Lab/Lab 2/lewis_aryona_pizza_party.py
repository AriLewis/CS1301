''' Pizza party, lots of inputs and identifying diff between floats and integers and also restricting the amount of decimals of floats.'''

people = int(input('Please enter the number of people attending the party: '))
pizza = int(input('PLease enter the number of pizzas purchased for the party: '))
diameter = int(input('Please enter the diameter of the pizzas: '))
slice = int(input('Please enter the number of slices per pizza: '))

area: float = 3.14*diameter
slices: int = pizza*slice
area_per: float  = area*people
slices_per: float = slice*people

print(f'The total pizza area: {area:.2f} square inches ')
print(f'Total number of slices: {slices}')
print(f'Pizza area per person: {area_per:.2f} square inches')
print(f'Slices per person: {slices_per:.2f}')
