import unittest
from PackageBNP.mon_module import addition


class AdditionTest(unittest.TestCase):
    def testSimpleAddition(self):
        res = addition(4, 6)
        self.assertEqual(res, 10)


if __name__ == "__main__":
    unittest.main()
