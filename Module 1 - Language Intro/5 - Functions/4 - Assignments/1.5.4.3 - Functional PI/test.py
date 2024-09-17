import math
def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI
    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    # Initialize variables as per the Gauss-Legendre algorithm
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 0.25
    p = 1.0
    pi_old = 0

    while True:
        # Perform the iterative steps
        a_next = (a + b) / 2.0
        b_next = math.sqrt(a * b)
        t_next = t - p * (a - a_next) ** 2
        p_next = 2 * p

        # Approximate value of PI
        pi_new = ((a_next + b_next) ** 2) / (4 * t_next)

        # Check if the approximation is within the target error bound
        if abs(pi_new - pi_old) < target_error:
            break

        # Update variables for the next iteration
        a = a_next
        b = b_next
        t = t_next
        p = p_next
        pi_old = pi_new

    return pi_new


desired_error = 1E-10
approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")