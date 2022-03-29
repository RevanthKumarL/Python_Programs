# python program to find factorial of a number
# tip = ctrl + `` to open the terminal for input related programs

def factorial(n):


    # single line to find the factorial
    return 1 if (n==1 or n ==0) else n * factorial(n-1);

    # driver code
num = 12;
print("Factorial of", num, "is", factorial(num))

