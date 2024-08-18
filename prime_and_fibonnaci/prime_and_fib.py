x = int(input())

fib = []

in_fib_seq = False

for i in range(x):
    if i == 0 or i == 1:
        fib.append(i)
    else:
        fib.append(fib[i-1] + fib[i - 2])


if x in fib:
    in_fib_seq = True

is_prime = True

for i in range(x):
    if i == 0:
        i =+ 1
    if x % i == 0 and x != i and i != 1:
        is_prime = False

if is_prime and in_fib_seq:
    print(x, "is a prime and in Fibonacci sequence")
elif is_prime and in_fib_seq ==False:
    print(x, "is a prime number and not in the Fibonacci sequence")
elif is_prime == False and in_fib_seq:
    print(x, "is not a prime number but is in the Fibonacci sequence")
else:
    print(x, "is not a prime or in the Fibonacci sequence")
