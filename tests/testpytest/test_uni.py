import unittest


class TestUni(unittest.TestCase):
    def setUp(self) -> None:
        self.adss = "dddd"
    def test_get_a(self):
        b = self.adss
        print(b)


if __name__ == "__main__":
    unittest.main()