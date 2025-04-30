# Task1 : Calculate factorial using a function

def factorial(n):
  if(n < 2):
    return 1
  else:
    return (n*(factorial(n-1)))
  
print(factorial(5))