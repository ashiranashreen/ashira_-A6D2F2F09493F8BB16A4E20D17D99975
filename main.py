def factorial(n):
  if n==0:
    return 1
  return n*factorial(n-1)
num=6
print("factorial of",num,"is",factorial(num))