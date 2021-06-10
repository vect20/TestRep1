from Monad import *
import unittest

argInt = 5
argFloat = 5.5
argStr = '5'

def sq(x):
    return x*x

def astr(x):
    return x + ' Test'

def afloat(x):
    return x*0.5

def dv(x):
    return x/0    

class TestMaybe(unittest.TestCase):
    def setUp(self):
        self.MaybeInt = MaybeInt(argInt)
        self.MaybeFloat = MaybeFloat(argFloat)
        self.MaybeStr = MaybeStr(argStr)

    def test_MaybeInt(self):
        self.assertEqual(Nothing(),Nothing())
        self.assertEqual(Nothing(),self.MaybeInt >> dv)
        self.assertEqual(MaybeInt(25), self.MaybeInt >> sq)
        self.assertNotEqual(MaybeInt(24), self.MaybeInt >> sq)
        self.assertEqual(Nothing(),self.MaybeInt >> astr >> sq)

    def test_MaybeFloat(self):
        self.assertEqual(Nothing(),self.MaybeFloat >> dv)
        self.assertEqual(MaybeFloat(30.25), self.MaybeFloat >> sq)
        self.assertNotEqual(MaybeFloat(30.1), self.MaybeFloat >> sq)
        self.assertEqual(MaybeFloat(2.75),self.MaybeFloat >> afloat)
        self.assertEqual(Nothing(),self.MaybeFloat >> astr >> afloat)

    def test_MaybeStr(self):
        self.assertEqual(Nothing(),self.MaybeStr >> dv)
        self.assertEqual(MaybeStr('5 Test'), self.MaybeStr >> astr)
        self.assertNotEqual(MaybeStr(' Test'), self.MaybeStr >> astr)
        self.assertEqual(Nothing(),self.MaybeStr >> afloat >> astr)
        
  

if __name__ == '__main__':
    unittest.main()        



