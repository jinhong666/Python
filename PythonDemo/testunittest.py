import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_even(self):
        '''
        Test that numbers between 0 and 5 ara all even
        :return:
        '''
        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i % 2 ,0)


if __name__ == '__main__':
    unittest.main()
