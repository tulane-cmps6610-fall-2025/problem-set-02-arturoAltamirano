"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
from tabulate import tabulate
import random

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    #base case: one of them is a single bit - return to break recursion 
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val
    
    #we need to continue recursion
    else:

        #we need to continue recursion, pad to get an even length before we split them
        x_array, y_array = pad(x.binary_vec, y.binary_vec)

        #split these into 4-quadrants and multiply all combinations 
        #this is where the quadratic runtime comes from - have to do 4 per iteration
        x_left, x_right = split_number(x_array)
        y_left, y_right = split_number(y_array)

        n = len(x_array)
    
        #left half of x and y
        product1 = quadratic_multiply(x_left, y_left)
        p1 = bit_shift(BinaryNumber(product1), n) 
    
        #right half of x and y
        product2 = quadratic_multiply(x_right, y_right)
        p2 = BinaryNumber(product2)   
    
        #left half of x and right half of y
        product3 = quadratic_multiply(x_left, y_right)
        
        #right half of x and left half of y
        product4 = quadratic_multiply(x_right, y_left)

        cross = BinaryNumber(product3 + product4)
        p3 = bit_shift(cross, n // 2)

        #(xL ​yL​) ⋅ 2n + (xL ​yR ​+ xR ​yL​) ⋅ 2n/2 + (xR ​yR​)
        return p1.decimal_val + p2.decimal_val + p3.decimal_val

def subquadratic_multiply(x, y):
    #base case: one of them is a single bit - return to break recursion 
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val
    
    #we need to continue recursion
    else:
        #pad to get an even length before we split them again
        x_array, y_array = pad(x.binary_vec, y.binary_vec)

        #split these into 4-quadrants and multiply all combinations 
        #this is where the quadratic runtime comes from - have to do 4 per iteration
        x_left, x_right = split_number(x_array)
        y_left, y_right = split_number(y_array)

        n = len(x_array)
    
        #left half of x and y
        product1 = subquadratic_multiply(x_left, y_left)
        p1 = bit_shift(BinaryNumber(product1), n) 
    
        #right half of x and y
        product2 = subquadratic_multiply(x_right, y_right)
        p2 = BinaryNumber(product2)  

        #Karatsuba's trick of instead adding these together
        #this makes 3 operations instead of 4, hence subquadratic
        product3 = subquadratic_multiply(
        BinaryNumber(x_left.decimal_val + x_right.decimal_val),
        BinaryNumber(y_left.decimal_val + y_right.decimal_val)
        )

        cross = product3 - product1 - product2
        p3 = bit_shift(BinaryNumber(cross), n // 2) 

    return p1.decimal_val + p2.decimal_val + p3.decimal_val

## Feel free to add your own tests here.
### I noticed the default binary2int displays the binary as well and will
### break the assertions, I dropped the call and structured the functions accordingly
### apologies if this is undesired, see the notebook for implementations that use the provided functions
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

test_multiply()

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)

def print_results(results):
    print("\n")
    print(
        tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
compare_multiply()

### custom built comparison - see notebook for details ###
def print_results(results):
    print("\n")
    print(
        tabulate(
            results,
            headers=['n', 'quadratic - bitwise generation', 'subquadratic - bitwise generation'],
            floatfmt=".3f",
            tablefmt="github"))

def compare_multiply():
    results = []
    qtimes = []
    subqtimes = []
    bit_sizes = [8, 16, 32, 64, 128, 256, 512, 1024]

    #test based on bit length with random numbers
    for bits in bit_sizes:
        #generate random numbers based on bit length
        #https://docs.python.org/3/library/random.html#:~:text=random.getrandbits,arbitrarily%20large%20ranges.
        n1 = random.getrandbits(bits)
        n2 = random.getrandbits(bits)
        bn1, bn2 = BinaryNumber(n1), BinaryNumber(n2)

        qtime = time_multiply(bn1, bn2, quadratic_multiply)
        subqtime = time_multiply(bn1, bn2, subquadratic_multiply)

        qtimes.append(qtime)
        subqtimes.append(subqtime)
        results.append((bits, qtime, subqtime))

    print_results(results)

    print(f"\nsub q times are on average : {round((sum(subqtimes) / sum(qtimes)) * 100)}% faster.")

compare_multiply()