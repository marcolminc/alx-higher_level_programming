#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit *= -1
print(f"Last digit of {number} is {digit} and is", end=' ')
if digit > 5:
    print('greater than 5')
elif digit == 0:
    print('0')
elif 6 > digit != 0:
    print('less than 6 and not 0')
