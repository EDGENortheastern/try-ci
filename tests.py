# test_prime_checker.py
import unittest
from main import is_prime

class TestPrimeChecker(unittest.TestCase):
    
    def test_prime(self):
        self.assertTrue(is_prime(5))   # 5 is a prime number
        self.assertTrue(is_prime(13))  # 13 is a prime number

    def test_non_prime(self):
        self.assertFalse(is_prime(4))   # 4 is not a prime number
        self.assertFalse(is_prime(1))   # 1 is not a prime number

    def test_negative_and_zero(self):
        self.assertFalse(is_prime(0))   # 0 is not a prime number
        self.assertFalse(is_prime(-7))  # Negative numbers are not prime

if __name__ == "__main__":
    unittest.main()
