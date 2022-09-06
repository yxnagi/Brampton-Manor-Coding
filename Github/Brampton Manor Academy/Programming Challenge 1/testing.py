import unittest

from main import *

class MyFirstTests(unittest.TestCase):

    def test_metres(self):
        self.assertEqual(convertmetres(10), 50.292)

    def test_furlong(self):
        self.assertEqual(convertfurlong(10), 0.25)

    def test_mile(self):
        self.assertEqual(convertmile(50.292), 0.03125007767)

    def test_foot(self):
        self.assertEqual(convertfoot(50.292), 165.0)

    def test_time(self):
        self.assertEqual(converttime(0.03125007767), 0.6048402129985564)


