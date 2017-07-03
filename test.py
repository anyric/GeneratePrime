""" Test class for prime function """
import unittest
import prime

class TestCheckisPrime(unittest.TestCase):
    """ Class to test checkisprime function """
    def test_check3isprime(self):
        """ test to asserts 3 is prime """
        self.assertEqual(prime.generate_prime_numbers(3), 3)

    def test_check7isprime(self):
        """ test to assert 7 is prime """
        self.assertEqual(prime.generate_prime_numbers(7), 7)

    def test_check9isnotprime(self):
        """ test to assert 9 is not prime """
        self.assertEqual(prime.generate_prime_numbers(9), 'None')

if __name__ == '__main__':
    unittest.main()
