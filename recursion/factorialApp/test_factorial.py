import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_typeError(self):
        with self.assertRaises(TypeError):
            factorial("5")
    
    def test_factorial_valueError(self):
        with self.assertRaises(ValueError):
            factorial(-3)

if __name__ == "__main__":
    unittest.main()