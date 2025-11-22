import unittest

class CalcTest(unittest.TestCase): 
    def test_plus(self):
        expected=1
        result=plus(3,2)
        self.assertEqual(result,expected,"錯誤：{}不等於{}" .format(result,expected))
        
    def test_minus(self):
        expected=1
        result=minus(3,2)
        self.assertEqual(result,expected) 
        
def plus(a,b):return a+b
def minus(a,b):return a-b        
        
if __name__ == '__main__':
    unittest.main()