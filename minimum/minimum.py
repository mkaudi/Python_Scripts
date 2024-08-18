x = float(input())
y = float(input())
z = float(input())
min = 0

if x < y or x == y:
    min = x
else:
    min = y

if z < min:
    min = z

print(min)
