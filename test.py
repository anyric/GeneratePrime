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
        
    def test_check11isprime(self):
        """ test to assert 11 is not prime """
        self.assertEqual(prime.generate_prime_numbers(11), 11)

    def test_check9isnotprime(self):
        """ test to assert 9 is not prime """
        self.assertEqual(prime.generate_prime_numbers(9), 'None')
        
    def test_check12isnotprime(self):
        """ test to assert 12 is not prime """
        self.assertEqual(prime.generate_prime_numbers(12), 'None')

if __name__ == '__main__':
    unittest.main()
