x = int(input())

is_prime = True

for i in range(x):
    if i == 0:
        i =+ 1
    if x % i == 0 and x != i and i != 1:
        is_prime = False


if is_prime == True:
    print(x, "is prime")
else:
    print(x, "is not prime")
