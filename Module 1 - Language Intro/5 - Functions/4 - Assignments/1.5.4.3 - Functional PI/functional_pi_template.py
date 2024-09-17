import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    pi_estimate = 0

    a = 1
    b = 1 / (2 ** (1 / 2))
    t = 1 / 4
    p = 1

    # perform 10 iterations of this loop
    for i in range(1, 10):
        """
        Step 2: Update each variable based upon the algorithm. Take care to ensure
        the order of operations and dependencies among calculations is respected. You
        may wish to create new "temporary" variables to hold intermediate results
        """

        a2 = (a + b) / 2
        b2 = (a * b) ** (1 / 2)
        p2 = 2 * p
        t2 = t - (p * (a2 - a) ** 2)
        a = a2
        b = b2
        p = p2
        t = t2
        print("new values", a2, b2, p2, t2)

        # print out the current loop iteration. This is present to have something in the loop.
        print("Loop Iteration: ", i)
        pi_estimate = ((a2 + b2) ** 2) / (4 * t2)

        print("Final estimate for PI: ", pi_estimate)
        print("Error on estimate: ", abs(pi_estimate - math.pi))
        return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
