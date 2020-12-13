from time import time
from functools import reduce
input = [
'1006605',
'19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
]

def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def proc(a, b):
	[_, x, y] = extended_euclid_gcd(a[1],b[1])
	return (a[0]*b[1]*y + b[0]*a[1]*x, a[1]*b[1])

if __name__ == '__main__':
	start = time()
	depart = int(input[0])
	(wait_time, busID) = min([(int(bus) - depart%int(bus), int(bus)) for bus in input[1].split(',') if bus != 'x'])
	print("Part 1: ", wait_time*busID)

	bang = [(-num%int(bus), int(bus)) for num,bus in enumerate(input[1].split(',')) if bus != 'x']
	(ans, mod) = reduce(proc, bang)
	print("Part 2: ", ans%mod)
	print(time() - start)