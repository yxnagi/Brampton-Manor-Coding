import unittest

from main import *

class MyFirstTests(unittest.TestCase):

    def test_energy(self):
        self.assertEqual(findenergy(1), 1995262.3149688789)

    def test_tnt(self):
        self.assertEqual(findtnt(1995262.3149688789), 0.00047687913837688307)

if __name__ == '__main__':
    unittest.main()

