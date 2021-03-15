import unittest
import os

from reverse import reverse

class Testdefreverse(unittest.TestCase):
    
    def test_reverse_is_reversing(self):
        self.assertEqual(reverse("test"))

if __name__ == '__main__':
    unittest.main()