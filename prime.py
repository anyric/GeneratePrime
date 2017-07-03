""" Function to determine whether a number is prime """


def isprime(numbers):
    """ Checks if a number has more than one factors """
    factors = True
    for i in range(2, numbers):
        if numbers% i == 0:
            factors = False
            break
    return factors

def generate_prime_numbers(numberlimit):
    """ Generates prime number from 0 to given number """
    #for number in range(0, numberlimit):
    if isprime(numberlimit):
        return numberlimit
    else:
        return 'None'

print(generate_prime_numbers(3))
