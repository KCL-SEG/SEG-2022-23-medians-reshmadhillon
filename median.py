"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
median = None
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
print(numbers)
halfsize = len(numbers)// 2
if len(numbers)%2 == 0:
    median = (numbers[halfsize] + numbers[halfsize -1])/2
    print(f'midpoint is: {halfsize}')
else:
    median = numbers[halfsize]
    print(f'midpoint is: {halfsize}')
print(numbers)
print(median)
