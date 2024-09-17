import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """





    pi_estimate = 0

    # modify these lines to correct set the variable values
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1


    for i in range(1, 10):


        a_equation = (a + b) / 2
        b_equation = (a * b) ** (1 / 2)
        p_equation = 2 * p
        t_equation = t - (p * (a_equation - a) ** 2)
        a = a_equation
        b = b_equation
        p = p_equation
        t = t_equation



        print("Loop Iteration: ", i)


    pi_estimate = ((a_equation + b_equation) ** 2) / (4 * t_equation)


    return pi_estimate
desired_error = 1E-10

pi_estimate = my_pi(desired_error)

print("Solution returned PI=", pi_estimate)

error = abs(math.pi - pi_estimate)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")