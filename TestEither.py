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

class TestEither(unittest.TestCase):
    def setUp(self):
        self.EitherInt = EitherInt(argInt)
        self.EitherFloat = EitherFloat(argFloat)
        self.EitherStr = EitherStr(argStr)

    
    def test_EitherInt(self):
        self.assertEqual(Left(5),Left(5))
        self.assertEqual(Left(argInt),self.EitherInt >> dv)
        self.assertEqual(EitherInt(25), self.EitherInt >> sq)
        self.assertNotEqual(EitherInt(24), self.EitherInt >> sq)
        self.assertEqual(Left(argInt),self.EitherInt >> astr >> sq)
        self.assertEqual(Left(argInt**4),self.EitherInt >> sq >> sq >> astr)
        

    def test_EitherFloat(self):
        self.assertEqual(Left(5.1),Left(5.1))
        self.assertEqual(Left(argFloat),self.EitherFloat >> dv)
        self.assertEqual(EitherFloat(argFloat**2), self.EitherFloat >> sq)
        self.assertNotEqual(EitherFloat(argFloat**2), self.EitherFloat >> afloat)
        self.assertEqual(Left(argFloat),self.EitherFloat >> astr >> sq)
        self.assertEqual(Left((argFloat**2/2)),self.EitherFloat >> sq >> afloat >> astr)

    def test_EitherStr(self):
        self.assertEqual(Left('s'),Left('s'))
        self.assertEqual(Left(argStr),self.EitherStr >> dv)
        self.assertEqual(EitherStr(argStr+' Test'), self.EitherStr >> astr)
        self.assertNotEqual(EitherStr(argStr), self.EitherStr >> astr)
        self.assertEqual(Left(argStr +' Test'),self.EitherStr >> astr >> sq)
        self.assertEqual(Left(argStr+ ' Test' +' Test'),self.EitherStr >> astr  >> astr >> sq)
        
  

if __name__ == '__main__':
    unittest.main()        