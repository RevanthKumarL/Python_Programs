# python to find factorial of a given number

def factorial(n):

    #single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

# driver code
num = 11
print ("Factorial of",num, "is", factorial(num))