import math

def sum_(a,b):
    m=a+b
    print(f"{a}+{b}={m}")
    return m

def subtrac(a,b):
    m=a-b
    print(f"{a}-{b}={m}")
    return m

def multi(a,b):
    m=a*b
    print(f"{a}*{b}={m}")
    return m
def divi(a,b):
    m=a/b
    print(f"{a}/{b}={m}")
    return m
    
def quotient(a,b):
    m=a//b
    print(f"The quotient of {a}/{b} is {m}")
    return m

def remainder(a,b):
    c=a%b
    print(f"The Remainder of {a}/{b} is",c)
    return c

def factadd(a):
    m=0
    for i in range(a,0,-1):
        m=m+i
    print(f"The sum of range 1 to {a} is {m}")
    return m
        

def power(a,b):
    m=a**b
    print(f"The value of {a} to the power {b} is {m}")
    return m


def naturalog(a):
    m=math.log(a)
    print(f"The natural log value of {a} is {m}")
    return m


def logb10(a):
    m=math.log10(a)
    print(f"The base 10 log value of {a} is {m}")
    return m


def logb2(a):
    m=math.log2(a)
    print(f"The base 2 log value of {a} is {m}")
    return m


def squareroots(a,b):
    m=(a**(1/2))
    print(f"The square root of {a} is {m}")
    return m


def factr(a):
    m=1
    for i in range(a,1,-1):
        m=m*i
    print(f"The factorial of {a} is {m}")
    return m
    
