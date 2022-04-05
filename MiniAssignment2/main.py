from math import factorial

n = int(input('Enter a number :'))

for i in range(n):
   for j in range(n):

      if(j>i):
         print('0',end="")
      else:
         print(factorial(i)//(factorial(j)*factorial(i-j)), end="")
   print("")