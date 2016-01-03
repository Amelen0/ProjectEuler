'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

import time

def factor(n):
  # Remove any factors of two
  factors = []
  
  while n % 2 == 0:
     factors.append(2) 
     n = n/2

  

