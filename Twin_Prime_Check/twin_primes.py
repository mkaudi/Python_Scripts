import math

def is_prime(x):
    # Complete the missing code here
    # The function takes in an integer and returns true
    # if it is prime. Otherwise, it returns false

    #set the prime variable to track whether it is a prime or not
    prime = True

    #loop to check if the number is a prime
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            prime = False
    return prime
        

def is_twin_prime(x):	
    # Complete the missing code. The function takes in 
    # an integer and returns true if it is a twin prime.
    # Otherwise, it returns false. Hint: The function should
    # make use of the is_prime() function in some way

    #check if prime and twin prime
    if is_prime(x):
        if is_prime(x-2) or is_prime(x+2):
            return True
    else:
        return False

	

N = int(input())
for i in range(N):
    p = int(input())
    if is_twin_prime(p):
        print("true")
    else:
        print("false")
