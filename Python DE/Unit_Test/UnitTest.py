import  unittest
from simple_calc import *
class TestMyFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_stringadd(self):
        pass

if __name__ == '__main__':
    unittest.main()
