x = int(input())

if x > 75:
    print('First')
elif x >= 70 and x < 75:
    print('Upper second')
elif x >= 60 and x < 70:
    print('Lower second')
elif x >= 50 and x < 60:
    print('Third')
else:
    print('Fail')
