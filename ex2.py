#Hello This is ex2.py of Project Euler


def fibonaccii(n):
   if n == 1 or n == 2:
      return 1

   return fibonaccii(n-1) + fibonaccii(n-2)

