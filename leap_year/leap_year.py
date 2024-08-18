x = int(input())

if x % 100 == 0:
    if x % 400 == 0:
        print(f'{x} is a leap year')
elif x % 4 == 0:
    print(f'{x} is a leap year')
else:
    print(f'{x} is not a leap year')
