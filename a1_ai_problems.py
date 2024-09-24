# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

#def factorial(n):

    #s = n
    #for i in range(1,n):
    #    s *= i
    #return s

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    el = 0
    el2 = 1
    for i in range(2, n+1):
        el = el2
        el2 = el+el2
    return el2




    

