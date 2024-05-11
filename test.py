import unittest
from para8_3 import *

class My_test(unittest.TestCase):


    def test_arg(self):
        self.assertEquals(adder(2 , 2), 4)


if __name__ == '__main__':
    unittest.main()
