# import unittest
# import math_operations

# class TestAddition(unittest.TestCase):
    
#     def test_add(self):
#         self.assertEqual(math_operations.add(2, 2), 4)

import unittest
from math_operations import add

class TestAddition(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()

