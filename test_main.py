import  unittest
from main import *

data = {'Смартфон':251,'Компьютер':340,'Планшет':36,'Тв':10}

class Test_main(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_test_arr(self):
        self.assertEqual(type(test_arr(data)),tuple)
    def test_percent1(self):
        self.assertEqual(type(percent([13,256,2])), list)
    def test_percent2(self):
        for i in percent([13,256,56]):
            with self.subTest(i=i):
                self.assertGreaterEqual(100,i)

if __name__ == '__main__':
    unittest.main()