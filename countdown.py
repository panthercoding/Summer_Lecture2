def buggy_countdown(n): #causes infinite recursion
  print("{} SECONDS LEFT".format(n))
  countdown(n-1)

def countdown(n):
  if (n <= 0):
    print("START")
  elif (n > 0):
    print("{} SECONDS LEFT".format(n))
    countdown(n-1)

countdown(10)