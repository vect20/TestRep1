from Monad import *
import unittest

argStrList = ['a','b','c']
argIntList = [1,2,3,4]
argFloatList = [2.5,3.75,5.25]

def sq(x):
    return x*x

def astr(x):
    return x + 'Test'

def afloat(x):
    return x*0.5

def dv(x):
    return x/0    

class TestMonadoList(unittest.TestCase):
    def setUp(self):
        self.MonadoListStr = MonadoList(argStrList)
        self.MonadoListInt = MonadoList(argIntList)
        self.MonadoListFloat = MonadoList(argFloatList)

    def test_MonadoListInt(self):
        self.assertEqual(MonadoList([]),self.MonadoListInt >> dv)
        self.assertEqual(MonadoList([1,4,9,16]),self.MonadoListInt >> sq)
        self.assertNotEqual(MonadoList([]),self.MonadoListInt >> sq >> sq)
        self.assertEqual(MonadoList([]),self.MonadoListInt >> astr)
        self.assertNotEqual(MonadoList([1,4,9,16]),self.MonadoListInt >> astr >> sq)
        self.assertEqual(MonadoList([1,16,81,256]),self.MonadoListInt >> sq >> sq)

    def test_MonadoListFloat(self):
        self.assertEqual(MonadoList([]),self.MonadoListFloat >> dv)
        self.assertEqual(MonadoList([6.25,14.0625,27.5625]),self.MonadoListFloat >> sq)
        self.assertNotEqual(MonadoList([]),self.MonadoListFloat >> sq >> sq)
        self.assertEqual(MonadoList([]),self.MonadoListFloat >> astr)
        self.assertNotEqual(MonadoList([6.25,14.0625,27.5625]),self.MonadoListFloat >> astr >> sq)
        self.assertEqual(MonadoList([0.625,0.9375,1.3125]),self.MonadoListFloat >> afloat >> afloat)        

    def test_MonadoListStr(self):
        self.assertEqual(MonadoList([]),self.MonadoListStr >> dv)
        self.assertEqual(MonadoList(['aTestTest','bTestTest','cTestTest']),self.MonadoListStr >> astr >> astr)
        self.assertEqual(MonadoList([]),self.MonadoListStr >> sq >> sq)
        self.assertEqual(MonadoList([]),self.MonadoListStr >> astr >> sq)


        

        
  

if __name__ == '__main__':
    unittest.main()     