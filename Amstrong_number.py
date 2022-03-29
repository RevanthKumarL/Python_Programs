# program to determine whether a number is armstrong number or not



def power(x, y):

    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2) * power(x, y // 2)

    # function to calculate order of the number
def order(x):
    # variable to store the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n
# function to check whether the given
# number is amstrong number or not
def isamstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

    # if condition satisfies
    return (sum1 == x)

# driver code
x = 153
print(isamstrong(x))

x = 1253
print(isamstrong(x))
