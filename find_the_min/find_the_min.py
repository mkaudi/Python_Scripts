x = int(input())
min = x

while x != -1:
    if x < min:
        min = x
    x = int(input())

print(min)
