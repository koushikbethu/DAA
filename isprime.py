import math

def isprime(n):
    if n<=1:
        return "No"
    if n==2:
        return "Yes"
    for i in range(3,int(math.sqrt(n)+1),2):
      if n%i==0:
        return "No"
    return "Yes"



n=int(input())
print(isprime(n))
