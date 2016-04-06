import math
import random

def get_pi(n=10000):
    """ 
    Simple function to calculate pi using monte carlo methods in a unit circle
    Args:
	n: number of iterations (default: 10000)
    Returns:
        tuple of (result, error estimate)    
    """    

    count_in = 0
    for i in range(0, n):    
        # here we generate a random (x,y) in [0,1) square 
        # and calculate hypotenuse
        h = math.hypot(random.random(), random.random())
        if (h < 1.0):
            count_in += 1
    return (4.0* count_in/n, 1.0/math.sqrt(n))

def main():
    n = 10000000
    print 'Calculating pi over %s iterations' % n
    (pi, exp_err) = get_pi(n)
    act_err = abs(pi - math.pi)
    print 'pi is %s, expected_error is %s, actual_error is %s' % (pi, exp_err, act_err) 

if __name__ == "__main__":
    main()
