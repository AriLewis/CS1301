age = int(input('Please enter your age:'))
weight = int(input('Please enter your weight in pounds:'))
heart = int(input('Please enter your heart rate in BPM:'))
time = int(input('Please enter the length of your workout in minutes:'))

calories = ((age*0.2757+weight*0.03295+heart*1.0781-75.4991)*time)/8.368

print(f'calories burned: {calories:.2f}')