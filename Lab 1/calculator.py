# calculator


import calculator as c

class FooCalculator:

    #empty constructor
    def __inti__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

    def subtract(selfm,m,n):
        return c.subtract(m,n)

    def multiply(self, m, n):
        return c.multiply(m,n)

def somma(m, n):
    print(str("sum(m, n) = "))
    res = m
    if n < 0:
        for i in range(abs(n)):
            res += 1
        print res
        return res
    else:
        for i in range(n):
            res += 1
        return res

def divide(m,n):
    count = 0
    negativeResult = m>0 and n<0 or m<0 and n>0
    n=abs(n)
    m=abs(m)

    while (m-n>=0):
        m -= n
        count +=1
    return int

def subtract(m, n):
    res = m
    if n < 0:
        for i in range(abs(n)):
            res -= 1
        return res
    else:
        for i in range(n):
            res += 1
        return res

def multiply(m,n):
    res = 0
    for i in range(n):
        res += sum(m, m)
    return res
