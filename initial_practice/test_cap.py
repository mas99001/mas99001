import unittest
import cap 

class TestCap(unittest.TestCase):
    def test_cap_text(self):
        self.assertEqual(cap.cap_text("hello"), "Hello")
        self.assertEqual(cap.cap_text("world"), "World")
        self.assertEqual(cap.cap_text(""), "")

if __name__ == "__main__":
    unittest.main()