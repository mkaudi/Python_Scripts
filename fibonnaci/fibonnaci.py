x = int(input())

fib = []

for i in range(x):
    if i == 0 or i == 1:
        fib.append(i)
    else:
        fib.append(fib[i-1] + fib[i - 2])

for j in fib:
    print(j, end=' ')

if x in fib:
    print("\n", x, "is in the Fibonacci sequence")
else:
    print("\n", x, "is not in the Fibonacci sequence")
