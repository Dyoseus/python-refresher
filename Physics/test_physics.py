import unittest
from physics import Physics


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(Physics.calculate_buoyancy(3, 4), 12)
        self.assertNotEqual(Physics.calculate_buoyancy(3, 4), 10)

    def test_calculate_float(self):
        self.assertEqual(Physics.will_it_float(3, 4), True)
        self.assertNotEqual(Physics.will_it_float(3, 4), False)

    def test_calculate_pressure(self):
        self.assertEqual(Physics.calculate_pressure(50), 490500)
        self.assertNotEqual(Physics.calculate_pressure(50), 500000)


if __name__ == "__main__":
    unittest.main()
