import sys 
import math

primes = []
for i in range (2, int(sys.argv[1])+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print(primes)
