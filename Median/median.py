import math

x = int(input())
y =[]

for i in range(x):
    x = int(input())
    y.append(x)

y.sort()

if len(y) % 2 != 0:
    print(y[int(len(y)/2)])
else:
    mid = len(y)/2
    median = (y[int(mid-1)] + y[int(mid-1)+1])/2
    print(median)


