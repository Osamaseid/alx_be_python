import unittest

# Buggy function to calculate the square of a number
def calculate_square(number):
    # Intentional bug: using addition instead of multiplication
    return number + number

class TestCalculateSquare(unittest.TestCase):
    
    def test_valid_input(self):
        self.assertEqual(calculate_square(2), 4)
        self.assertEqual(calculate_square(3), 9)
        self.assertEqual(calculate_square(0), 0)
        self.assertEqual(calculate_square(-2), 4)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_square("a string")
        with self.assertRaises(TypeError):
            calculate_square(None)
        with self.assertRaises(TypeError):
            calculate_square([1, 2, 3])

# Run the tests
if __name__ == "__main__":
    unittest.main()
