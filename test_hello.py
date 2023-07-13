import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertNotEqual(hello.sin(90), 1)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertNotEqual(hello.cos(2), 1)

    def test_tan(self):
       self.assertEqual(hello.tan(0), 0)
       self.assertEqual(hello.tan(1), 1.5574077246549023)
       self.assertNotEqual(hello.tan(2), 1)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertNotEqual(hello.cot(2), 1)

    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(4, 2), 6)
        self.assertNotEqual(hello.add(1, 10), 19)

    def test_sub(self):
        self.assertEqual(hello.sub(1, 2), -1)
        self.assertEqual(hello.sub(4, 2), 2)
        self.assertNotEqual(hello.sub(1, 10), -8)

    def test_mul(self):
        self.assertEqual(hello.mul(1, 2), 2)
        self.assertEqual(hello.mul(4, 2), 8)
        self.assertNotEqual(hello.mul(1, 10), 3)

    def test_div(self):
        self.assertEqual(hello.div(1, 2), 0.5)
        self.assertEqual(hello.div(4, 2), 2)
        self.assertNotEqual(hello.div(1, 10), 5)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)
        self.assertNotEqual(hello.sqrt(16), 5)

    def test_power(self):
        self.assertEqual(hello.power(1, 2), 1)
        self.assertEqual(hello.power(2, 3), 8)
        self.assertNotEqual(hello.power(4, 2), 4)

    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(5), 1.6094379124341003)
        self.assertNotEqual(hello.log(3), 1)


    def test_exp(self):
        self.assertEqual(hello.exp(1), 2.718281828459045)
        self.assertEqual(hello.exp(5), 148.4131591025766)
        self.assertNotEqual(hello.exp(3), 19)

if __name__ == "__main__":
    unittest.main()
