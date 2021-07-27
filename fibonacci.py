def Fibonacci(n):
  if (n == 0):
    return(0)
  elif (n==1):
    return(1)
  
  else:
    return Fibonacci(n-1) + Fibonacci(n-2)

#fib_answers is a dictionary containing already computed Fibonacci values
def smartFibonacci(n,fib_answers):
  if (n in fib_answers): #nth fibonacci number already computed
    return fib_answers[n]
  
  else:
    fib_value = smartFibonacci(n-1,fib_answers) + smartFibonacci(n-2,fib_answers)
    #store the nth Fibonacci number in the dictioary for future usage
    fib_answers[n] = fib_value
    
    return(fib_value) #retunr the nth fibonacci value

fib_answers = {}

#we know the first two Fibonacci numbers are 0 and 1
fib_answers[0] = 0
fib_answers[1] = 1

for n in range(50): #calculates the first 50 Fibonacci numbers
  print("{}th Fibonacci Number = {}".format(n,smartFibonacci(n,fib_answers)))