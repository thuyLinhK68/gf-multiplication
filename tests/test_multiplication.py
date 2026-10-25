
import unittest

from gf2m4 import multiply as multiply4
from gf2m8 import multiply as multiply8


class TestGaloisFieldMultiplication(unittest.TestCase):

    def test_gf4_example(self):
        self.assertEqual(multiply4(0b1011, 0b0101), 0x1)

    def test_gf8_example(self):
        self.assertEqual(multiply8(0x57, 0x83), 0xC1)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply4(0, 7), 0)
        self.assertEqual(multiply8(0, 123), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply4(1, 7), 7)
        self.assertEqual(multiply8(1, 123), 123)

    def test_commutative(self):
        self.assertEqual(multiply4(3, 5), multiply4(5, 3))
        self.assertEqual(multiply8(0x57, 0x83),
                         multiply8(0x83, 0x57))


if __name__ == "__main__":
    unittest.main()
