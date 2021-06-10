from Monad import *
import unittest


argStr = '5'
argStr1 = '5Test'

def sq(x):
    return x*x

def astr(x):
    return x + 'Test'

def afloat(x):
    return x*0.5

def dv(x):
    return x/0    

class TestIO(unittest.TestCase):
    def setUp(self):
        self.IO = IO(argStr)

    def test_IO(self):
        self.assertEqual(IO_false("IO Monad error: unsupported operand type(s) for /: 'str' and 'int'"),self.IO >> dv)
        self.assertEqual(IO(argStr1), self.IO >> astr)
        self.assertNotEqual(IO(argStr1 + 's'), self.IO >> astr)
        self.assertEqual(IO_false("IO Monad error: can't multiply sequence by non-int of type 'float'"),self.IO >> afloat >> astr)
        
  

if __name__ == '__main__':
    unittest.main()     