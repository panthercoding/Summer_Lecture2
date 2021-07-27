def factorial(n):
  if (n == 0):
    return 1
  else:
    return n*factorial(n-1)

for n in [0,1,2,3,4,5,6]:
  print("{}! = {}".format(n,factorial(n)))