import sys
from math import sqrt

def factor(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    div = 3
    sqroot = int(sqrt(number)) + 1
    while number > 1:
        if number % div == 0:
            number /= div
            factors.append(div)
            sqroot = int(sqrt(number)) + 1
        else:
            div += 2
            if div > sqroot:
                factors.append(int(number))
                number = 1
    if len(factors) <= 1:
        return ' is a prime number'
    else:
        return factors


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        number = sys.argv[1]
        if number.isdigit(): 
            print number, factor(int(number))
        else:
            print 'Is "%s" actually a positive natural number?' % number
    else:
        for number in sys.stdin.readlines():
            try:
                print number, factor(int(number))
            except ValueError, e:
                print e.message

