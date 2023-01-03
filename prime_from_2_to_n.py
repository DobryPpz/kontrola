import sys
import math

def is_prime(n):
    if(n<2):
        return False
    if(n==2):
        return True
    limit = math.ceil(math.sqrt(n))
    for i in range(2,limit+1):
        if(n%i==0):
            return False
    return True

for i in range(2,int(sys.argv[1])+1):
    if(is_prime(i)):
        print(i)
