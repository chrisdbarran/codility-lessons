""" Test the codility module
"""
import unittest
import codility



class TestCodility(unittest.TestCase):
    def testPermCheckValid(self):
        self.assertEqual(codility.permCheck([4,1,3,2]),1) 


    def testPermCheckInValid(self):
        self.assertEqual(codility.permCheck([4,1,3]),0)

    def testPermCheckSingleElementNotOne(self):
        self.assertEqual(codility.permCheck([4]),0)

    def testPermCheckSingleElementIsOne(self):
        self.assertEqual(codility.permCheck([1]),1)

    def testPermCheckDoubleElementConsecutiveNotOne(self):
        self.assertEqual(codility.permCheck([4,5]),0)

    def testPermCheckTwoElementsConsecutive(self):
        self.assertEqual(codility.permCheck([1,2]),1)

    def testPermCheckTwoElementsNonConsecutive(self):
        self.assertEqual(codility.permCheck([1,6]),0)

if __name__ == '__main__':
    unittest.main()