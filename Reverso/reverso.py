x = input()
y = []

while x != "###":
    y.append(x)
    x = input()

z = len(y)-1
for i in y:
    print(y[z])
    z = z - 1
