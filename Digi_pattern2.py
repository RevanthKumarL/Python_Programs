n = 673828
x = []
while n>0:
    x.append(n%10)
    n //= 10
for i in range(len(x)-1,-1,-1):
    print('|'+x[i]*'*')
    # don't understand a single fuck over here