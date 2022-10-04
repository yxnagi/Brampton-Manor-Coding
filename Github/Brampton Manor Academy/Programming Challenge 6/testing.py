import unittest

from main import *

class MyFirstTests(unittest.TestCase):

    def make_square(self):
        self.assertEqual((3, 1), [[1, 2, 3], [2, 3, 1], [3, 1, 2]])

if __name__ == '__main__':
    unittest.main()

