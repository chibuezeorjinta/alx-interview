import unittest
#from '0x00-pascal_triangle.0-pascal_triangle' import pascal_triangle as triangle
triangle = __import__('0-pascal_triangle').pascal_triangle

class TestTriangle(unittest.TestCase):
    def test_badinput(self):
        empty = triangle(-2)
        self.assertEqual(empty, [])
        
if __name__ == '__main__':
    unittest.main()