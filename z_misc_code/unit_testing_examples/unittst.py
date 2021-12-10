import unittest

def add(x,y):
    return x + y

class MyTest(unittest.TestCase):

    def test(self):
      self.assertEqual(add(3,4), 8)

    def test2(self):
        self.assertEqual(add(3,4), 7)

    def test_split(self):
        s = 'hello world'
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(1)

    def test_true(self):
        self.assertTrue('FOo'.isupper())

    def test_in(self):
        self.assertIn('1', ['2', 7, 'a', '1'])

if __name__ == '__main__':
    unittest.main()