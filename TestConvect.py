from Monad import *
import unittest
   
class TestConvect(unittest.TestCase):
    def test_Convect(self):
        self.assertEqual(convectM(5,MaybeInt),MaybeInt(5))
        self.assertEqual(convectM(5,MaybeFloat),MaybeFloat(5.0))
        self.assertEqual(convectM('5',MaybeStr),MaybeStr('5'))
        self.assertEqual(convectM(5,EitherFloat),EitherFloat(5.0))
        self.assertEqual(convectM(5,EitherInt),EitherInt(5))
        self.assertEqual(convectM('5',EitherStr),EitherStr('5'))
        self.assertEqual(convectM(5,ErrorFloat),ErrorFloat(5.0))
        self.assertEqual(convectM(5,ErrorInt),ErrorInt(5))
        self.assertEqual(convectM('5',ErrorStr),ErrorStr('5'))
        self.assertEqual(convectM('5',IO),IO('5'))
        self.assertEqual(convectM([1,2,3],MonadoList),MonadoList([1,2,3]))

if __name__ == '__main__':
    unittest.main()     