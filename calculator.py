def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    if(y==0):
        return -1 # failure case, division should not be possible when denominator is 0. Error should be shown.
    return x/y 

def sqrt(x):
    if(x<0):
        return -1 # failure case, square root should not be possible when number is negative. Error should be shown.
    return math.sqrt(a)
