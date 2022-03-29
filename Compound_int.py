# A = P(1+R/1000)*t
# Compound interest = A-P

def compound_interest(principle, rate, time):

    # claculates the compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Amount lent is ", Amount)
    print("Compound Interest is", CI)
    
# driver code
compound_interest(100000, 11.7, 5)


