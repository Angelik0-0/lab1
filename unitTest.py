import unittest
import math

import sys
sys.path.insert(0, 'C:\\Users\\Ира\\PycharmProjects\\pythonProjectt')


for p in sys.path:
    print(p)

import square

class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(10), 100)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(10), 40)



if __name__ == '__main__':
    unittest.main()