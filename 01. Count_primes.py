"""
Given an integer n, return the number of prime numbers that are strictly less than n.

"""

def countPrimes(n):
  """
    :type n: int
    :rtype: int
  """
  count = 1
  if n==0 or n==1 or n==2:
    return 0
  for i in range(2,n):   
    for j in range(2,i):    
        if i % 2 == 0:
            break
        elif i % j == 0:
            break
        elif j == i-1: 
            count+=1
  return count

n=countPrimes(1000)       
print("Ans:",n)     # Ans: 168   