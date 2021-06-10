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

class TestError(unittest.TestCase):
    def setUp(self):
        self.ErrorInt = ErrorInt(argInt)
        self.ErrorFloat = ErrorFloat(argFloat)
        self.ErrorStr = ErrorStr(argStr)

    def test_ErrorInt(self):
        self.assertEqual(Failure(ZeroDivisionError,5),self.ErrorInt >> dv)
        self.assertEqual(ErrorInt(25), self.ErrorInt >> sq)
        self.assertNotEqual(ErrorInt(24), self.ErrorInt >> sq)
        self.assertEqual(Failure(TypeError,5),self.ErrorInt >> astr >> sq)

    def test_ErrorFloat(self):
        self.assertEqual(Failure(ZeroDivisionError,5.5),self.ErrorFloat >> dv)
        self.assertEqual(ErrorFloat(30.25), self.ErrorFloat >> sq)
        self.assertNotEqual(ErrorFloat(30.1), self.ErrorFloat >> sq)
        self.assertEqual(ErrorFloat(2.75),self.ErrorFloat >> afloat)
        self.assertEqual(Failure(TypeError,2.75),self.ErrorFloat >> afloat >> astr )

    def test_ErrorStr(self):
        self.assertEqual(Failure(TypeError,'5'),self.ErrorStr >> dv)
        self.assertEqual(ErrorStr('5 Test'), self.ErrorStr >> astr)
        self.assertNotEqual(ErrorStr(' Test'), self.ErrorStr >> astr)
        self.assertEqual(Failure(TypeError,'5'),self.ErrorStr >> afloat >> astr)
  

if __name__ == '__main__':
    unittest.main()