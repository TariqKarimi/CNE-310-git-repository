def sumTo():
    """ Return the sum of reciprocals of powers of 2 """

    theSum  = 0
    aNumber = 0
    while theSum < 2.0:
        theSum = theSum + 1/2**aNumber
        aNumber = aNumber + 1

    return theSum

print(sumTo())
