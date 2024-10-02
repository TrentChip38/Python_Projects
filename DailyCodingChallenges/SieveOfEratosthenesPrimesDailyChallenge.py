#The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
#The method is to take increasingly larger prime numbers, and mark their multiples as composite.
#For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
#then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, 
#the unmarked numbers that remain will be prime.
#Implement this algorithm.
#Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

def Sieve(N):
    #figure out every prime up to N
    primes = []
    for i in range(2, N+1):
        isprime = 1
        #print("I: ", i)
        for prime in primes:
            #print("Check: ", prime)
            rem = i%prime
            #print("Rem", rem)
            if (rem == 0):
                #If divisible, not prime
                isprime = 0
        if (isprime):
            #if not divisible by any, then prime
            #print("Prime: ", i)
            primes.append(i)
    return primes

#this one gets rid of unesesary division and is quicker
def sieve(N):
    #figure out every prime up to N
    primes = []
    for i in range(2, N+1):
        isprime = 1
        #print("I: ", i)
        for prime in primes:
            #print("Check: ", prime)
            rem = i%prime
            #print("Rem", rem)
            if (rem == 0):
                #if divisible, not prime
                isprime = 0
                break
        #if not divisible, is prime
        if isprime:
            primes.append(i)
    return primes

#test
print(sieve(1000000))